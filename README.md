# Sentinel-Portal-MSS
Senior Capstone Team 4 Project ITEC 27217-03 with Dr. Neil Rigole at Middle Georgia State University Spring 2026 

Project: Cybersecurity Monitoring & Incident Response Portal for Medical Sight Security

PLEASE READ >>>

-------------START GUIDE HERE----------------

Need the following installed on your local machine:
        Python
        MySQL Server and MySQL Workbench

Database Initialization:
        1) Open MySQL Workbench.
        2) Open and execute the schema.sql file provided in this repository.
        3) This will create the sentinel_db database and the event_logs table required for data persistence.

Change Credentials in Files:
Because this is a prototype, you must update your local database password 
        1) Open both app.py and simulated_attack.py.
        2) Locate the CONFIGURATION block at the top of each file.
        3) Update the DB_PASSWORD variable to match your local MySQL root password.

Install:
Navigate to the project folder in your terminal and install the required Python libraries:
        pip install flask mysql-connector-python

Run the Application:
        1) Start the Backend: In your terminal, run python app.py.
        2) Access the Dashboard: Open a web browser and navigate to http://127.0.0.1:5000.
        3) Trigger a Security Event: While the dashboard is open, open a second terminal and run python simulated_attack.py.

------END OF START GUIDE--------
