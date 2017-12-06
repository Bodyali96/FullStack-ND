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

    items = session.query(Item).order_by(Item.id.desc()).limit(10)
    category_items = session.query(Item).order_by(Item.id.desc()).limit(10)
    app.logger.info(category_items)
    return render_template('catalog.html', categories=categories, category_items=zip(items, category_items))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
