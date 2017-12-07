from flask import Flask, render_template, url_for, redirect, flash
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
    category = session.query(Category).filter(Category.name == category_name).one()
    item = session.query(Item).filter_by(category_id=category.id, name=item_name).one()
    return render_template('item_card.html', categories=categories, category_name=category_name, item=item)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
