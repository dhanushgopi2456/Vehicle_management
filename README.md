# 🚗 Vehicle Management System

<p align="center">
  <b>A Flask-Powered Web Application for Efficient Vehicle Management</b>
  <br/>
  Manage vehicle records, user accounts, and route searches through a simple, database-driven web interface.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" alt="Flask"/>
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white" alt="SQLite"/>
  <img src="https://img.shields.io/badge/HTML5-Frontend-E34F26?logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3&logoColor=white" alt="CSS3"/>
</p>

---

## 📌 Overview

The **Vehicle Management System** is a web application developed using Python and Flask to simplify vehicle record management and user administration. It integrates an SQLite database to store and retrieve vehicle information efficiently.

The application provides user registration, login, vehicle CRUD operations, vehicle search, and separate admin and user interfaces.

## ✨ Key Features

- 🔐 **User Authentication** — Registration and login functionality.
- 🚘 **Vehicle Management** — Add, view, update, and delete vehicle records.
- 🔎 **Vehicle & Route Search** — Search for vehicle information and access route-search functionality.
- 👥 **Role-Based Interfaces** — Separate admin and user pages.
- 🗄️ **SQLite Integration** — Lightweight, persistent database storage.
- 🎨 **Template-Based UI** — Dynamic HTML pages rendered using Flask and Jinja2.
- ⚡ **CRUD Operations** — Efficient management of vehicle records.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Backend web framework |
| HTML5 & CSS3 | User interface and styling |
| Jinja2 | Dynamic HTML templating |
| SQLite | Relational database |
| Git & GitHub | Version control and repository hosting |

## 🏗️ Project Architecture

```text
Vehicle_Management/
│
├── instance/
│   └── vehicle_management.db
│
├── templates/
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
├── createdb.py
├── vip.py
└── README.md
```

**Main components**

- `vip.py` — Main Flask application containing the web routes and application logic.
- `createdb.py` — Initializes the SQLite database and its required tables.
- `templates/` — Contains HTML templates for authentication, vehicle management, and user interfaces.
- `instance/vehicle_management.db` — Stores application data locally.

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/dhanushgopi2456/Vehicle_management.git
```

### 2. Navigate to the project directory

```bash
cd Vehicle_management
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Initialize the database

```bash
python createdb.py
```

### 5. Start the application

```bash
python vip.py
```

### 6. Open the application

Visit the following URL in your browser:

**http://127.0.0.1:5000/**

## 💡 Core Functionalities

| Module | Description |
|---|---|
| Authentication | Register and log in to the application |
| Admin Dashboard | Access the administrative interface |
| Vehicle Management | Create, view, update, and delete vehicle records |
| Vehicle Search | Find relevant vehicle information |
| Route Search | Access the route-search page |
| Database | Persist vehicle and application records using SQLite |

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building web applications using Python and Flask.
- Implementing database connectivity with SQLite.
- Developing CRUD operations for structured records.
- Rendering dynamic web pages with Jinja2 templates.
- Organizing backend routes and frontend templates.
- Understanding authentication and role-based application design.

## 🔮 Future Enhancements

- 🛡️ Strengthen authentication and authorization.
- 🗺️ Integrate interactive maps and route optimization.
- 📱 Improve responsive design for mobile devices.
- 📊 Add vehicle statistics and dashboard analytics.
- ☁️ Deploy the application to a cloud platform.
- 🧪 Add automated tests and input validation.

## 👨‍💻 Developed By

**Dhanush Gopi Kavala**

Computer Science Engineer | Full-Stack Developer | AI/ML Enthusiast

<p align="center">
  <a href="https://github.com/dhanushgopi2456">GitHub Profile</a>
  &nbsp; • &nbsp;
  <a href="https://www.linkedin.com/in/dhanush-gopi-kavala-a460a528b/">LinkedIn</a>
</p>

---

<p align="center">
  ⭐ If you find this project useful, consider giving the repository a star!
  <br/>
  <b>Built with Python, Flask, and SQLite.</b>
</p>
