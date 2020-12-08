from flask import *
import MySQLdb.cursors
from HelpMethods import *
from flask_mysqldb import MySQL

# DATABASE BLOCK START#
app = Flask(__name__)
mysql = MySQL(app)
# DATABASE BLOCK ENDS#
#
#
#
#
OrderPage = Blueprint('OrderPage', __name__, static_folder='static', template_folder='templates')

@OrderPage.route("/order")
def order():
    return "<h1>Order</h1>"