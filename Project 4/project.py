from flask import Flask, render_template, url_for, redirect, flash


app = Flask(__name__)


categories = [{'name': 'Soccer', 'id': '1'},
            {'name': 'Basketball', 'id': '2'},
            {'name': 'Baseball', 'id': '3'},
            {'name': 'Frisbee', 'id': '4'},
            {'name': 'Snowboarding', 'id': '5'},
            {'name': 'Rock Climbing', 'id': '6'},
            {'name': 'Foosball', 'id': '7'},
            {'name': 'Skating', 'id': '8'},
            {'name': 'Hockey', 'id': '9'}]
items = [{'name': 'Stick',
          'description': '',
          'category': '9',
          'id': '1'},
         {'name': 'Goggles',
          'description': '',
          'category': '5',
          'id': '2'},
         {'name': 'Snowboard',
          'description': '',
          'category': '5',
          'id': '3'},
         {'name': 'Two shinguards',
          'description': '',
          'category': '1',
          'id': '4'},
         {'name': 'Shinguards',
          'description': '',
          'category': '1',
          'id': '5'},
         {'name': 'Frisbee',
          'description': '',
          'category': '4',
          'id': '6'},
         {'name': 'Bat',
          'description': '',
          'category': '3',
          'id': '7'},
         {'name': 'Jersey',
          'description': '',
          'category': '1',
          'id': '8'},
         {'name': 'Soccer Cleats',
          'description': '',
          'category': '1',
          'id': '9'}]


@app.route('/')
@app.route('/catalog')
def show_catalog():
    return render_template('catalog.html', categories=categories, items=items)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
