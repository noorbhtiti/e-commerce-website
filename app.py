import os

from flask import *
from datetime import timedelta
import MySQLdb.cursors
from flask_admin import Admin, AdminIndexView, form # admin
from flask_admin.contrib.sqla import ModelView  # admin
from flask_admin.menu import MenuLink  # admin
#from flask.ext.admin.form.upload import FileUploadField # admin
from flask_admin.form.upload import ImageUploadField
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy  # admin
from wtforms.validators import ValidationError
from HelpMethods import *
from UsersViews import UsersViews
from LoginPage import LoginPage
from RegisterPage import RegisterPage
from ProfilePage import ProfilePage
from shoppingbag import shoppingbag
from OrderPage import OrderPage
from PlaceOrderPage import PlaceOrderPage
from wtforms import SelectField

app = Flask(__name__)

app.register_blueprint(UsersViews, url_prefix="")  # www.youtube.com/watch?v=WteIH6J9v64
app.register_blueprint(LoginPage, url_prefix="")
app.register_blueprint(RegisterPage, url_prefix="")
app.register_blueprint(ProfilePage, url_prefix="")
app.register_blueprint(shoppingbag, url_prefix="")
app.register_blueprint(OrderPage, url_prefix="")
app.register_blueprint(PlaceOrderPage, url_prefix="")

app.secret_key = 'thisKeyIsSoSecret'
app.permanent_session_lifetime = timedelta(minutes=500)  # session time

app.config['MYSQL_HOST'] = 'utbweb.its.ltu.se'
app.config['MYSQL_USER'] = '941227'
app.config['MYSQL_PASSWORD'] = '941227'
app.config['MYSQL_DB'] = 'db941227'

# admin
basedir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(basedir, 'static')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://941227:941227@utbweb.its.ltu.se/db941227'
app.config['FLASK_ADMIN_SWATCH'] = 'Cyborg'  # http://bootswatch.com/3/ för att bälja swatches # admin panel
db = SQLAlchemy(app)
db.Model.metadata.reflect(bind=db.engine, schema='db941227')


class User(db.Model):
    # skapa en model på en befintlig tabell!!!!!!!!!!!
    __table__ = db.Model.metadata.tables['db941227.Users']

    def __repr__(self):
        return "%s, %s" % (self.FirstName, self.UserID)


class Categorys(db.Model):
    __table__ = db.Model.metadata.tables['db941227.Categorys']

    def __repr__(self):
        return "%s, %s" % (self.CategoryName, self.CategoryID)


class Cart(db.Model):
    Products_ID = db.relationship("Product", backref="Cart")
    User_ID = db.relationship("User", backref="Cart")
    __table__ = db.Model.metadata.tables['db941227.Cart']

    #def __repr__(self):
    #    return self.UserID


class CartView(ModelView):
    column_list = ("User_ID", "Products_ID", "Amount")
    form_columns = ["User_ID", "Products_ID", "Amount", ]

    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class Orders(db.Model):
    User_ID = db.relationship("User", backref="Orders")
    __table__ = db.Model.metadata.tables['db941227.Orders']

    #def __repr__(self):
    #    return self.UserID


class OrdersView(ModelView):
    column_list = (
    "User_ID", "OrderID", "Amount", "OrderStatus", "ShippingAdress", "OrderPhoneNumber", "OrderEmail", "DataOfOrder")
    # form_columns = ["User_ID", "Amount", "OrderStatus", "ShippingAdress", "OrderPhoneNumber", "OrderEmail", "DataOfOrder",]
    can_create = False

    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class CategorysView(ModelView):
    column_display_pk = True
    form_columns = ["CategoryName", "Image"]

    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class ProductsCategory(db.Model):
    # skapa en model på en befintlig tabell!!!!!!!!!!!
    Products_ID = db.relationship("Product", backref="ProductsCategory")
    Categorys_ID = db.relationship("Categorys", backref="ProductsCategory")
    __table__ = db.Model.metadata.tables['db941227.ProductsCategory']

    def __repr__(self):
        return '<User %r>' % self.ProductID


class ProductsCategoryView(ModelView):
    column_list = ("Products_ID", "Categorys_ID")
    form_columns = ["Products_ID", "Categorys_ID", ]

    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class AdminUser(db.Model):
    # skapa en model på en befintlig tabell!!!!!!!!!!!
    __table__ = db.Model.metadata.tables['db941227.Admin']

    def __repr__(self):
        return '<User %r>' % self.Email


class Product(db.Model):
    # skapa en model på en befintlig tabell!!!!!!!!!!!
    __table__ = db.Model.metadata.tables['db941227.Products']

    def __unicode__(self):
        return self.ProductName

    def __repr__(self):
        return "%s, %s" % (self.ProductName, self.ProductID)


class ProductView(ModelView):
    form_excluded_columns = ("Rating",)
    form_columns = ["ProductName", "ProductPrice", "NumberInStock", "Description", "imageName", ]
    column_display_pk = True

    form_extra_fields = {
        'imageName': form.ImageUploadField(
            'Image', base_path=file_path, thumbnail_size=(100, 100, True))
    }

    def on_model_change(self, form, model, is_created):
        proudctNum = int(form.NumberInStock.data)
        ProductPrice = int(form.ProductPrice.data)
        print(proudctNum)
        if proudctNum < 0:
            print('noooooooooooooooo')
            raise ValidationError(str(proudctNum) + " Number in stock cannot be less than 0 !")
        if ProductPrice < 0:
            print('yeeees')
            raise ValidationError(str(ProductPrice)+ " Product price cannot be less than 0!")
        return model

    def delete_model(self, model):
        x = str(model).split(", ")
        x = x[len(x)-1]
        print(x)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            print(x)
            cursor.execute('DELETE FROM Products WHERE ProductID = %s', (x,))
            mysql.connection.commit()
            print("deleted")
            return True
        except:
            print("EXCEPT")
            return False
        finally:
            print("FINALLY")
            cursor.close()


    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class AdminIndexView(AdminIndexView):
    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:  # Gets in except if email is not in session, meaning that the user is not logged in
            return False
        return False  # This returns false only if a user is logged in, but not admin


class UserView(ModelView):
    column_searchable_list = ('Email', "FirstName", "LastName", "PhoneNumber")
    form_columns = ["FirstName", "LastName" ,"PhoneNumber" ,"Email" ,"Password" ,"Adress",]
    def is_accessible(self):
        try:
            email = uppercase(session['email'])
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return True
        except:
            return False
        return False


class AdminUserView(ModelView):
    column_display_pk = True  # optional, but I like to see the IDs in the list
    column_hide_backrefs = False
    column_list = ('Email', "DateOfAdmin")
    form_excluded_columns = ("DateOfAdmin",)  # Remove the dateofadmin because its automatic in myphpadmin
    column_searchable_list = ('Email',)
    edit_columns = ["Email", ]

    def on_model_change(self, form, model, is_created):
        email = uppercase(str(form.Email.data))
        # print(email)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE Email = %s', (email,))
        account = cursor.fetchone()
        if not account:
            raise ValidationError(email + " is not a user!")

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Admin WHERE Email = %s', (email,))
        account = cursor.fetchone()
        if account:
            raise ValidationError(email + " is already an Admin!")
        form.Email.data = email
        return model

    def is_accessible(self):
        try:
            if session["email"]:  ## ISTÄLLER FÖR session["email"] så måste vi
                return True
        except:
            return False
        return False


#    def inaccessible_callback(self, name, **kwargs):
#       # redirect to login page if user doesn't have access
#      return redirect(url_for('home')

admin = Admin(app, name="NOUELI", template_mode="bootstrap3", index_view=AdminIndexView())
# print("ADMIN ENDPOINT: "+ str(db.Model.__tablename__))
admin.add_view(UserView(User, db.session))
admin.add_view(AdminUserView(AdminUser, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(CategorysView(Categorys, db.session))
admin.add_view(ProductsCategoryView(ProductsCategory, db.session))
admin.add_view(CartView(Cart, db.session))
admin.add_view(OrdersView(Orders, db.session))
admin.add_link(MenuLink(name='Profile', category='', url="/profile"))
admin.add_link(MenuLink(name='Logout', category='', url="/logout"))
# END ADMIN

mysql = MySQL(app)


@app.route("/verify")
def verify():
    return render_template("verify.html")


if __name__ == '__main__':
    app.run(debug=True)