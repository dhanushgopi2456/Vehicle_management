from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicle_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class User(db.Model):
    userid = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    phoneno = db.Column(db.String(15), nullable=False)
class Vehicle(db.Model):
    vehicleid = db.Column(db.Integer, primary_key=True)
    vehiclename = db.Column(db.String(100), nullable=False)
    userid = db.Column(db.String(50), db.ForeignKey('user.userid'), nullable=False)
    city = db.Column(db.String(50), db.ForeignKey('user.city'), nullable=False)
def insert_admin():
    admin = User(userid='admin', password='admin', email='admin@admin.com', city='AdminCity', phoneno='0000000000')
    db.session.add(admin)
    db.session.commit()
if __name__ == '__main__':
    with app.app_context():  
        db.create_all()       
        if not User.query.filter_by(userid='admin').first():
            insert_admin()
        print("Database created and admin user added.")
