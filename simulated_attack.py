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
DB_PASSWORD = "Annajack9$" # <--- Change this
DB_NAME = "sentinel_db"
# =================================================================


#Simulated attack using python
import mysql.connector

def trigger_simulation():
    """
    Connects to the database and inserts a high-severity security event.
    This simulates the moment a malicious action is detected on the network.
    """
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        
        # Logic for a simulated brute-force attack on a medical IoT device
        sql = "INSERT INTO event_logs (source_ip, device_id, event_type, severity_level, access_status) VALUES (%s, %s, %s, %s, %s)"
        values = ("192.168.1.105", "HEART_MON_COCHRAN_01", "Brute Force Attempt", "Critical", "Denied")
        
        # Execute the transaction
        cursor.execute(sql, values)
        conn.commit()
        
        print("Simulation Successful: Security event injected into database.")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

if __name__ == "__main__":
    trigger_simulation()
