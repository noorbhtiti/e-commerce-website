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
shoppingbag = Blueprint('shoppingbag', __name__, static_folder='static', template_folder='templates')


@shoppingbag.route('/cart')
def cart():
    logged = False
    try:
        if session['email']:
            logged = True
    except:
        logged = False

    if logged:
        return render_template('shoppingbag.html', logged=logged)

    else:
        msg = "Please login to see cart"
        return render_template('login.html', errormsg=msg)
