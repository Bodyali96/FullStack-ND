from flask import Flask, render_template, url_for, redirect, flash, request, jsonify, make_response
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from urllib3.connectionpool import xrange

from database_setup import Base, Category, Item, User
from flask import session as login_session
import random, string, httplib2, json, requests
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog Application"

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/catalog/JSON')
def catalog_json():
    """Provides JSON endpoint of Catalog"""
    # Selecting all categories
    cat = session.query(Category).all()
    # Serializing categories
    endpoint = {'Category': [c.serialize for c in cat]}
    # Looping through categories, adding items of each category
    for j in endpoint['Category']:
        cat_items = session.query(Item).filter_by(category_id=j['id']).all()
        j['Item'] = [c.serialize for c in cat_items]
    # Writing JSON endpoint to catalog.json file
    with open('catalog.json', 'w') as jsonfile:
        json.dump(endpoint, jsonfile)
    return jsonify(endpoint)


@app.route('/')
@app.route('/catalog')
def show_catalog():
    """Viewing Categories and Latest Items"""
    # Selecting latest items by getting latest 10 id's
    latest_items = session.query(Item).order_by(Item.id.desc()).limit(10)
    return render_template('catalog.html', categories=categories(), latest_items=latest_items)


@app.route('/catalog/<string:category_name>/Items')
def show_category_items(category_name):
    """Viewing Items of a specific category"""
    # Selecting a category by name
    category = session.query(Category).filter_by(name=category_name).one()
    # Selecting items by category id
    items = session.query(Item).filter_by(category_id=category.id).all()
    return render_template('category_items.html', categories=categories(), items=items, category_name=category_name)


@app.route('/catalog/<string:category_name>/<string:item_name>')
def show_item(category_name, item_name):
    """Viewing an Item of a specific category"""
    # Selecting a category by name
    category = session.query(Category).filter_by(name=category_name).one()
    # Selecting an item by category id and item name
    item = session.query(Item).filter_by(category_id=category.id, name=item_name).one()
    return render_template('item_card.html', categories=categories(), category_name=category_name, item=item)


@app.route('/catalog/<string:category_name>/new', methods=['GET', 'POST'])
def create_item(category_name):
    """Creating an Item within specific category"""
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        # Adding post request details into database
        item = Item(name=request.form['name'],
                    description=request.form['description'],
                    category_id=request.form['category'],
                    user_id=request.form['user'])
        session.add(item)
        session.commit()
        # Redirecting page to a specific category added into it
        return redirect(url_for('show_category_items', category_name=category_name))
    # Otherwise render form page
    return render_template('new_item.html', category_name=category_name, categories=categories())


@app.route('/catalog/item/new', methods=['GET', 'POST'])
def create_item_default():
    """Creating an Item from home page without pre-selecting category"""
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        # Adding post request details into database
        item = Item(name=request.form['name'],
                    description=request.form['description'],
                    category_id=request.form['category'],
                    user_id=request.form['user'])
        session.add(item)
        session.commit()
        # Redirecting page to a specific category added into it
        return redirect(url_for('show_category_items', category_name=item['category']['name']))
    # Otherwise render form page
    return render_template('new_item_home.html', categories=categories())


@app.route('/catalog/<string:category_name>/<string:item_name>/edit', methods=['GET', 'POST'])
def edit_item(category_name, item_name):
    """Editing a specific Item within specific category"""
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(name=category_name).one()
    item_to_edit = session.query(Item).filter_by(category_id=category.id, name=item_name).one()
    if request.method == 'POST':
        # Adding post request details to be edited in database
        if request.form['name']:
            item_to_edit.name = request.form['name']
        if request.form['description']:
            item_to_edit.description = request.form['description']
        if request.form['category']:
            item_to_edit.category_id = request.form['category']
        session.add(item_to_edit)
        session.commit()
        # Selecting a category by id input from form
        category = session.query(Category).filter_by(id=request.form['category']).one()
        # Redirecting page to a specific category added into it
        return redirect(url_for('show_category_items', category_name=category.name))
    # Otherwise render form page
    return render_template('edit_item.html', category_name=category_name, item_name=item_name, categories=categories(), item=item_to_edit)


@app.route('/catalog/<string:category_name>/<string:item_name>/delete', methods=['GET', 'POST'])
def delete_item(category_name, item_name):
    """Deleting a specific Item withing specific category"""
    if 'username' not in login_session:
        return redirect('/login')
    # Selecting category by name
    category = session.query(Category).filter_by(name=category_name).one()
    # Selecting item to be deleted by category name and item name
    item_to_delete = session.query(Item).filter_by(category_id=category.id, name=item_name).one()
    if request.method == 'POST':
        session.delete(item_to_delete)
        session.commit()
        # Redirecting page to a specific category deleted from it
        return redirect(url_for('show_category_items', category_name=category_name))
    # Otherwise render confirmation page
    return render_template('delete_item.html', category_name=category_name, item_name=item_name, categories=categories(), item=item_to_delete)


@app.route('/catalog/find', methods=['GET', 'POST'])
def find_items():
    """Finding Items by text between words"""
    # If input form has search text
    if request.method == 'POST' and 'search' in request.form:
        # Select items like that text
        items = session.query(Item).filter(Item.name.like('%'+request.form['search']+'%')).all()
        return render_template('find_items.html', items=items, categories=categories())
    return redirect(url_for('show_catalog'))


def categories():
    """Selecting all categories from database"""
    categories_list = session.query(Category).all()
    return categories_list



# Create anti-forgery state token
@app.route('/login')
def show_login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/connect', methods=['POST'])
def googleConnect():
    # Ensure that the request is not a forgery and that the user sending
    # this connect request is the expected user.
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    req = h.request(url, 'GET')[1]
    req_json = req.decode('utf8').replace("'", '"')
    result = json.loads(req_json)    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('User is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    # First User to login gets administrator status
    if session.query(User).first().name == 'Mostafa Elsheikh':
        user = session.query(User).first()
        user.email = data['email']
        user.name = data['name']
        session.add(user)
        session.commit()
        login_session['email'] = user.email
        login_session['name'] = user.name
        login_session['id'] = user.id
    else:
        # See if user is a passed user if not create account
        findUser = session.query(User).filter(User.email == data['email'])
        if findUser.first():
            login_session['email'] = findUser.one().email
            login_session['name'] = findUser.one().name
            login_session['id'] = findUser.one().id
        else:
            newUser = User(email=data['email'],
                           name=data['name'])
            session.add(newUser)
            session.commit()
            login_session['email'] = newUser.email
            login_session['name'] = newUser.name

    response = make_response(json.dumps('Successfully connected user.'), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/disconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        flash('Current user not connected.')
        return redirect(url_for('showCatalog'))
    access_token = credentials
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's session.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['email']
        del login_session['name']
        del login_session['admin']

        flash('Successfully Logout.')
        return redirect(url_for('showCatalog'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# User Helper Functions
def create_user(login_session):
    newUser = User(name=login_session['username'], email=login_session[
        'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


if __name__ == '__main__':
    app.secret_key = 'bGdHShtVckfeLgHEl8UpXGBy'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
