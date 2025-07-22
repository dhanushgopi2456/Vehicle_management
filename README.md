# 🚗 Vehicle Management System

This project is a **Vehicle Management System** designed to help organizations or users efficiently manage vehicle-related data such as vehicle registration, updates, and maintenance records. It provides a streamlined interface for both users and administrators to manage vehicle information with ease.

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, JSP
- **Backend**: Java (Servlets)
- **Database**: MySQL
- **Server**: Apache Tomcat
- **IDE**: Eclipse / IntelliJ IDEA

## ✨ Key Features

### 👤 User Functions
- Vehicle registration with details (number, type, owner)
- View existing vehicle entries
- Edit or update vehicle data
- Delete vehicle record

### 🛠 Admin Functions
- Admin login and dashboard
- Full CRUD operations on all vehicle entries
- View all registered vehicles
- Delete invalid or old records

## 📂 Project Structure

Vehicle_management/
├── src/
│ ├── com/
│ │ └── vehicle/servlet/
│ ├── dao/
│ ├── model/
│ └── util/
├── WebContent/
│ ├── CSS/
│ ├── JSP/
│ ├── images/
│ └── index.jsp
├── vehicle_db.sql
├── README.md
└── ...


## ⚙️ Getting Started

### Prerequisites

- Java JDK 8+
- Apache Tomcat (v9 or later)
- MySQL Server
- Eclipse IDE (or any Java IDE with servlet support)

### Steps to Run

1. **Clone the Repository**
```bash
git clone https://github.com/dhanushgopi2456/Vehicle_management

Import Project

Open Eclipse → File → Import → Existing Projects into Workspace → Select this repo

Configure Server

Right-click Project → Run on Server → Choose Tomcat

Setup MySQL

Import vehicle_db.sql into your MySQL database.

Update DB credentials in your code (usually in DBUtil.java).

Run the Application

Visit http://localhost:8080/Vehicle_management in your browser

🧠 Future Enhancements
Add vehicle service & maintenance tracking

Role-based authentication (Admin vs User)

Vehicle insurance reminders

PDF export for vehicle reports

👨‍💻 Developed By
Dhanush Gopi Kavala
B.Tech | Java Full-Stack Developer | AI-ML Intern
