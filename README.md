# 🚗 Vehicle Management System

A Flask-based web application for managing vehicle details, user registrations, and route search functionalities with an integrated SQLite database.

## ✨ Features
- User registration and login system
- Add, update, and delete vehicle records
- Search and display vehicle details
- Role-based access for admin and users
- SQLite database integration

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (Jinja2 templates)
- **Database:** SQLite

## 📂 Project Structure
- `vip.py` → Main Flask application
- `createdb.py` → Script to set up database
- `templates/` → HTML templates for UI
- `instance/vehicle_management.db` → Database fill

Vehicle_Management/
│
├── instance/
│   └── vehicle_management.db      # SQLite database
│
├── templates/                     # HTML templates
│   ├── addvehicle.html
│   ├── admin.html
│   ├── deletevehicle.html
│   ├── displayvehicle.html
│   ├── login.html
│   ├── register.html
│   ├── response.html
│   ├── searchroute.html
│   └── user.html
│
├── __pycache__/                   # Compiled Python files
│   └── createdb.cpython-312.pyc
│
├── createdb.py                    # Script to initialize database
├── vip.py                         # Main Flask application file
├── README.md                      # Project documentation

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/dhanushgopi2456/Vehicle_management.git

Navigate to the project folder:

cd Vehicle_management


Install dependencies:

pip install flask


Initialize the database:

python createdb.py

Run the application:

python vip.py
Open in browser: http://127.0.0.1:5000/

👤 Developed By
Dhanush Gopi Kavala

