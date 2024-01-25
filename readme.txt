This document provides instructions on compiling, building, and installing the Library Management System (LMS) application.

1. Technical Dependencies:

Language: Python
Framework: Django
Database: MySQL
Web Technologies: HTML, CSS, Bootstrap, JQuery, JavaScript
Libraries: pymysql, mysqlclient, pandas
Operating System: Compatible with Windows, Linux, and macOS

2. Installation Steps:
a. Python Installation:
- Ensure Python is installed on your system. If not, download and install Python from python.org.
b. Django Installation:
- Open a terminal or command prompt.
- Run the command: pip install Django.
c. MySQL Database Setup:
- Install MySQL server and create a new database for the LMS.
- Update the database configuration in settings.py with your MySQL credentials.
d. Library Dependencies:
- Install required libraries using the following commands:
pip install pymysql 
pip install mysqlclient
pip install pandas


e. Project Setup:
- After you full fill the above requirements, Extract the provided zip file.
f. Navigate to Project Directory:
- Open a terminal/command prompt and navigate to the LMS project directory.
g. Connection between database and GUI
- To set up the connection between the database and the frontend code, follow these steps:
1. Open a terminal or command prompt.
2. Navigate to the directory where the frontend code is located.
For database setup:
3. Go to the directory where createTables.py and initializeTables.py present and run the command `python createTables.py` to create the necessary database tables.
4. Execute `python initializeTables.py` to populate the database with initial data.
h. Migrate Database:
- Go to the library directory where manage.py present and Run the following commands:
python manage.py makemigrations
python manage.py migrate
i. Run the Application:
- Execute the command: python manage.py runserver
- The application will be accessible at http://localhost:8000 in your web browser.
3. Usage Guide:
Follow the Quick Start Guide provided in the documentation for an overview of the application's features and functionalities.
4. Notes:
Ensure the MySQL server is running before starting the application.
Make sure to fulfill all requirements before proceeding with the setup.


