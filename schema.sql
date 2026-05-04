/*  Sentinel Portal - Version 1.0
  Author: AnnaRoseGS (Anna Schumaker/Bowker)
  Note: Initial framework and boilerplate assisted by AI; 
      all system logic and security implementation finalized by author.
*/


/* Initialize the Sentinel Database
   Ensure the database is created if it does not already exist.
*/
CREATE DATABASE IF NOT EXISTS sentinel_db;
USE sentinel_db;

/* The event_logs table is the core repository for all monitored activity.
   It stores timestamps, device identifiers, and severity metrics 
   to allow for historical analysis and real-time alerting.
*/
CREATE TABLE event_logs (
    /* Unique identifier for each log entry */
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    
    /* Records the exact time the event was written to the database */
    event_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    /* The origin IP of the network activity */
    source_ip VARCHAR(45),
    
    /* Identifier for the specific piece of medical hardware (e.g., HEART_MON_01) */
    device_id VARCHAR(50),
    
    /* Description of the behavior (e.g., Brute Force, Unauthorized Access) */
    event_type VARCHAR(100),
    
    /* Categorizes the threat level for visual prioritization on the dashboard */
    severity_level ENUM('Low', 'Medium', 'High', 'Critical'),
    
    /* Tracks whether the system blocked or allowed the attempted action */
    access_status VARCHAR(20)
);

/* Sample data insertion to verify the dashboard can pull 
   initial records upon first launch.
*/
INSERT INTO event_logs (source_ip, device_id, event_type, severity_level, access_status) 
VALUES ('127.0.0.1', 'SYSTEM_CORE', 'Initial System Check', 'Low', 'Allowed');
