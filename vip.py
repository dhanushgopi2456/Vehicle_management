from flask import Flask, render_template, request, redirect, url_for
from createdb import db, User, Vehicle
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicle_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 
with app.app_context():
    db.create_all()
@app.route('/')
def home():
    return redirect(url_for('login'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        user = User.query.filter_by(userid=userid).first()
        if user and user.password == password:
            if userid == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard', user=userid))
        else:
            return "Invalid credentials. Please try again.", 401
    return render_template('login.html')
@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin.html', admin='admin')

@app.route('/user_dashboard/<user>')
def user_dashboard(user):
    return render_template('user.html', user=user)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        email = request.form['email']
        city = request.form['city']
        phoneno = request.form['phoneno']
        new_user = User(userid=userid, password=password, email=email, city=city, phoneno=phoneno)
        db.session.add(new_user)
        db.session.commit()
        return render_template('response.html', message="User created successfully!")
    return render_template('register.html')
@app.route('/addvehicle', methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'POST':
        vehiclename = request.form['vehiclename']
        city = request.form['city']
        userid = request.form['userid']  # Get selected user from the form

        new_vehicle = Vehicle(vehiclename=vehiclename, userid=userid, city=city)
        db.session.add(new_vehicle)
        db.session.commit()
        return render_template('response.html', message="Vehicle added successfully!")
    users = User.query.all()  
    return render_template('addvehicle.html', users=users)
@app.route('/viewvehicle')
def view_vehicle():
    vehicles = Vehicle.query.all()
    return render_template('displayvehicle.html', vehicles=vehicles)
@app.route('/searchroute', methods=['GET', 'POST'])
def search_route():
    vehicles = []  
    city = None   
    if request.method == 'GET':
        city = request.args.get('city')
        if city:
            vehicles = Vehicle.query.filter_by(city=city).all()  
    return render_template('searchroute.html', vehicles=vehicles, city=city)
@app.route('/deletevehicle', methods=['GET', 'POST'])
def delete_vehicle():
    if request.method == 'POST':
        vehicleid = request.form['vehicleid']
        vehicle = Vehicle.query.get(vehicleid)
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
            return render_template('response.html', message="Vehicle deleted successfully!")
        else:
            return render_template('response.html', message="Vehicle not found.")
    vehicles = Vehicle.query.all()
    return render_template('deletevehicle.html', vehicles=vehicles)

@app.route('/logout')
def logout():
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
