from flask import Flask, render_template, url_for, redirect, flash, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

app = Flask(__name__)


engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog')
def show_catalog():
    categories = session.query(Category).all()
    latest_items = session.query(Item).order_by(Item.id.desc()).limit(10)
    return render_template('catalog.html', categories=categories, latest_items=latest_items)


@app.route('/catalog/<string:category_name>/Items')
def show_category_items(category_name):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category_id=category.id).all()
    return render_template('category_items.html', categories=categories, items=items, category_name=category_name)


@app.route('/catalog/<string:category_name>/<string:item_name>')
def show_item(category_name, item_name):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(category_id=category.id, name=item_name).one()
    return render_template('item_card.html', categories=categories, category_name=category_name, item=item)


@app.route('/catalog/<string:category_name>/new', methods=['GET', 'POST'])
def create_item(category_name):
    if request.method == 'POST':
        item = Item(name=request.form['name'],
                    description=request.form['description'],
                    category_id=request.form['category'],
                    user_id=request.form['user'])
        session.add(item)
        session.commit()
        return redirect(url_for('show_category_items', category_name=category_name))
    categories = session.query(Category).all()
    return render_template('new_item.html', category_name=category_name, categories=categories)


@app.route('/catalog/item/new', methods=['GET', 'POST'])
def create_item_default():
    if request.method == 'POST':
        item = Item(name=request.form['name'],
                    description=request.form['description'],
                    category_id=request.form['category'],
                    user_id=request.form['user'])
        session.add(item)
        session.commit()
        return redirect(url_for('show_category_items', category_name=item['category']['name']))
    categories = session.query(Category).all()
    return render_template('new_item_home.html', categories=categories)


@app.route('/catalog/<string:category_name>/<string:item_name>/edit', methods=['GET', 'POST'])
def edit_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item_to_edit = session.query(Item).filter_by(category_id=category.id, name=item_name).one()
    if request.method == 'POST':
        if request.form['name']:
            item_to_edit.name = request.form['name']
        if request.form['description']:
            item_to_edit.description = request.form['description']
        if request.form['category']:
            item_to_edit.category_id = request.form['category']
        session.add(item_to_edit)
        session.commit()
        return redirect(url_for('show_category_items', category_name=category_name))
    categories = session.query(Category).all()
    return render_template('edit_item.html', category_name=category_name, item_name=item_name, categories=categories, item=item_to_edit)


@app.route('/catalog/<string:category_name>/<string:item_name>/delete', methods=['GET', 'POST'])
def delete_item(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item_to_delete = session.query(Item).filter_by(category_id=category.id, name=item_name).one()
    if request.method == 'POST':
        session.delete(item_to_delete)
        session.commit()
        return redirect(url_for('show_category_items', category_name=category_name))
    categories = session.query(Category).all()
    return render_template('delete_item.html', category_name=category_name, item_name=item_name, categories=categories, item=item_to_delete)


@app.route('/catalog/find', methods=['GET', 'POST'])
def find_items():
    if request.method == 'POST' and 'search' in request.form:
        items = session.query(Item).filter(Item.name.like('%'+request.form['search']+'%')).all()
        return render_template('find_items.html', items=items)
    return redirect(url_for('show_catalog'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
