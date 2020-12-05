from flask import *
from flask_mysqldb import MySQL

# DATABASE BLOCK START#
app = Flask(__name__)
mysql = MySQL(app)
# DATABASE BLOCK ENDS#
#
#
#
#
cart = Blueprint('cart', __name__, static_folder='static', template_folder='templates')


@cart.route('/cart')
def cart():
    return render_template('cart.html')
