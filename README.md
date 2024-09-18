# Musketeers
Introduction
This project is a Django-based application for managing volunteers and charities. It includes functionality for filtering and displaying volunteers and charities based on different criteria.

Setup Instructions
Prerequisites
Python 3.11
Django 5.1.1
Virtual Environment 
Installation
Clone the Repository


git clone https://github.com/noysaadon/Musketeers.git
cd Musketeers
Create and Activate a Virtual Environment


python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install Dependencies


pip install -r requirements.txt
Apply Migrations


python manage.py migrate
Running the Data Script
Before starting the server, you need to run the script_dummies.py to populate the database with some initial data. Follow these steps:

Run the Data Script


python script_dummies.py
This script will create sample users, companies, volunteers, and charities in the database.

Running the Server
After running the data script, you can start the Django development server:

Start the Server


python manage.py runserver
Access the Application

Open your web browser and navigate to http://127.0.0.1:8000 to see the application in action.