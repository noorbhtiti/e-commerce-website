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
CartPage = Blueprint('CartPage', __name__, static_folder='static', template_folder='templates')


@CartPage.route('/cart')
def CartPage():
    return render_template('cart.html')
