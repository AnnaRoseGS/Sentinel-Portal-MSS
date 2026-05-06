"""
Sentinel Portal - Version 1.0
Author: AnnaRoseGS (Anna Schumaker/Bowker)
Note: Initial framework and boilerplate assisted by AI; 
      all system logic and security implementation finalized by author.
"""

# =================================================================
# CONFIGURATION - PLEASE UPDATE FOR YOUR LOCAL ENVIRONMENT
# =================================================================
# Dr. Rigole: Please update these credentials to match your local 
# MySQL instance before running the application.
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "YOUR_PASSWORD_HERE"
DB_NAME = "sentinel_db"
# =================================================================



#Flask file and python logic
from flask import Flask, render_template, jsonify
import mysql.connector

# Initialize Flask with a 'flat' directory structure
# template_folder='.' and static_folder='.' allow index.html and style.css 
# to reside in the same folder as this script.
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

# Database connection utility
# This function manages the handshake between Python and the MySQL server.
def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# ROUTE: Home Page
# Serves the main dashboard interface (index.html).
@app.route('/')
def index():
    return render_template('index.html')

# ROUTE: API Endpoint for Alerts
# This endpoint returns the 10 most recent security events in JSON format.
# The frontend JavaScript calls this to update the dashboard without refreshing.
@app.route('/api/alerts')
def get_alerts():
    try:
        conn = get_db_connection()
        # dictionary=True returns rows as key-value pairs for easy JSON conversion
        cursor = conn.cursor(dictionary=True)
        
        # SQL query to fetch the latest threats first
        query = "SELECT * FROM event_logs ORDER BY event_timestamp DESC LIMIT 10"
        cursor.execute(query)
        
        alerts = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Return the data to the frontend
        return jsonify(alerts)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start the local development server
    app.run(debug=True)
