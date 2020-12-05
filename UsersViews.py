from flask import *
from datetime import timedelta
import MySQLdb.cursors
from HelpMethods import *
from flask_sqlalchemy import SQLAlchemy  # admin
from flask_mysqldb import MySQL

UsersViews = Blueprint('UsersViews', __name__, static_folder='static', template_folder='templates')

# DATABASE BLOCK START# 
app = Flask(__name__)
mysql = MySQL(app)


# DATABASE BLOCK ENDS#


# home block start#
@UsersViews.route('/')
def home():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False
    return render_template('index.html', logged=logged)


# home block end#
#
#
#
#
# shop block start#
@UsersViews.route('/shop')
def shop():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM Products')
    prods = cursor.fetchall()
    print(prods)
    return render_template('Shop.html', logged=logged, prods=prods)

# shop block end#


###<p>Desc: {{prod['Description']}}</p>##