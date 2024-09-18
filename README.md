# Musketers
Introduction
This project is a Django-based application for managing volunteers and charities. It includes functionality for filtering and displaying volunteers and charities based on different criteria.

Setup Instructions
Prerequisites
Python 3.11
Django 5.1.1
Virtual Environment (recommended)
Installation
Clone the Repository

""bash
Copy code
git clone <repository_url>
cd <repository_directory>
Create and Activate a Virtual Environment

""bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install Dependencies

""bash
Copy code
pip install -r requirements.txt
Apply Migrations

""bash
Copy code
python manage.py migrate
Running the Data Script
Before starting the server, you need to run the script_dummies.py to populate the database with some initial data. Follow these steps:

Run the Data Script

""bash
Copy code
python script_dummies.py
This script will create sample users, companies, volunteers, and charities in the database.

Running the Server
After running the data script, you can start the Django development server:

Start the Server

""bash
Copy code
python manage.py runserver
Access the Application

Open your web browser and navigate to http://127.0.0.1:8000 to see the application in action.

Usage
Navigate to different pages using the links in the navigation bar.
Use the dropdown menu to filter volunteers and charities based on the criteria you need.
Contributing
Feel free to open issues and submit pull requests. Contributions are welcome!
