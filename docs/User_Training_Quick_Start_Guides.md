# User Training Documentation: Quick Start Guides

**Project:** Sentinel Monitoring & Incident Response Portal  
**Course:** ITEC 4750 - Capstone Project  
**Team:** Team 4  
**Organization:** Medical Sight Security (MSS)  
**Date:** May 5, 2026

## Document Purpose

This training document provides short, role-based quick start guides for the Sentinel Monitoring & Incident Response Portal. It is designed to support the final report appendix and explain how hospital staff, security analysts, administrators, and demonstration operators would use or support the system.

> **Prototype Scope Note:** The submitted GitHub prototype demonstrates a simplified MVP workflow: simulated security event generation, MySQL storage, Flask retrieval, and dashboard display. Login, MFA, role-based access, incident tickets, analyst notes, and the full normalized ERD are included as proposed full-system design elements or simulated training concepts.

## Table of Contents

1. [Training Overview](#1-training-overview)
2. [Quick Start Guide: General Hospital Staff](#2-quick-start-guide-general-hospital-staff)
3. [Quick Start Guide: Security Analyst](#3-quick-start-guide-security-analyst)
4. [Quick Start Guide: IT Administrator / System Maintainer](#4-quick-start-guide-it-administrator--system-maintainer)
5. [Quick Start Guide: Prototype Demonstration Operator](#5-quick-start-guide-prototype-demonstration-operator)
6. [Severity Levels and Response Expectations](#6-severity-levels-and-response-expectations)
7. [Troubleshooting and Escalation](#7-troubleshooting-and-escalation)
8. [Training Completion Checklist](#8-training-completion-checklist)

---

## 1. Training Overview

The Sentinel Monitoring & Incident Response Portal is designed to give hospital security staff centralized visibility into suspicious activity. The system uses simulated event data to demonstrate how login attempts, device activity, and suspicious access patterns can be stored, reviewed, and displayed through a dashboard interface.

Training is divided by user role so each group only focuses on the functions and security responsibilities that apply to them.

| Audience | Primary Training Goal | Key Topics |
|---|---|---|
| General Hospital Staff | Use secure access habits and report suspicious activity. | MFA awareness, phishing, badge/smart-card safety, reporting procedures |
| Security Analysts | Monitor alerts and investigate suspicious events. | Dashboard review, severity levels, event details, incident response workflow |
| IT Administrators | Maintain the application, database, and supporting environment. | MySQL, Flask, backups, access controls, dependency updates |
| Demo Operator | Run the MVP prototype for presentation or testing. | `schema.sql`, `app.py`, `simulated_attack.py`, dashboard verification |

### Training Assumptions

- No real patient data, live hospital logs, or production credentials should be used during training or demonstration.
- Training examples should use fictitious users, simulated device identifiers, and test IP addresses.
- The MVP demonstrates event monitoring and dashboard visibility; the full system would add operational login, MFA, role-based access, incident assignment, analyst notes, and live data sources.

---

## 2. Quick Start Guide: General Hospital Staff

This guide is for doctors, nurses, lab staff, administrative staff, and other hospital employees who may interact with protected systems or report suspicious activity. General staff members are not expected to manage the Sentinel dashboard, but their secure behavior directly affects the quality of monitoring and incident prevention.

### Before You Begin

- Use only your assigned workstation, badge, smart card, or approved login method.
- Do not share passwords, MFA codes, badges, smart cards, or workstation sessions.
- Lock your screen before leaving a workstation, even for a short period.
- Report missing badges, smart cards, or suspicious messages immediately.

### Secure Login and MFA Habits

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Open the approved hospital application or workstation login page. | Login page displays normally. |
| 2 | Enter your assigned username and password. | System prompts for the second authentication factor when required. |
| 3 | Enter the MFA code from your approved device or token. | Access is granted only after verification. |
| 4 | Never provide the MFA code to another person, even if the request appears urgent. | Account remains protected from credential theft and social engineering. |
| 5 | Lock the workstation when finished or when stepping away. | Unauthorized users cannot access the active session. |

### Report Suspicious Activity

Report immediately if you see:

- Unexpected MFA prompts
- Repeated login failures
- A missing badge or smart card
- Unusual workstation behavior
- Ransomware warnings
- Suspicious emails
- Requests for passwords, MFA codes, or credentials

When reporting, include:

- Your name
- Your location
- Workstation or device name, if known
- Approximate time observed
- What happened
- Whether patient care systems are affected

Do not investigate on your own. Leave technical review to IT/security staff so logs and evidence are preserved.

> **General Staff Rule of Thumb:** If something asks for your password, MFA code, badge, smart card, or urgent login approval and it feels unusual, stop and report it. Fast reporting is better than quiet guessing.

---

## 3. Quick Start Guide: Security Analyst

This guide is for M-COC or security operations staff who monitor alerts, review event details, and coordinate incident response. In the MVP, the dashboard displays simulated security events. In the proposed full system, analysts would also manage incident status, assignment, and notes.

### Dashboard Review Workflow

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Open the Sentinel dashboard from an approved workstation or demo browser. | The dashboard loads the current event list. |
| 2 | Review the newest events first and check severity labels. | Critical and high-severity activity is prioritized. |
| 3 | Identify the event type, source IP, device ID, timestamp, and access status. | The analyst can understand what happened and where it originated. |
| 4 | Compare repeated events or failed attempts from the same source. | Possible brute-force attempts or abnormal behavior can be identified. |
| 5 | Escalate critical events according to the incident response plan. | Security response begins quickly and consistently. |

### Analyst Review Checklist

- Confirm the timestamp and whether the event is recent.
- Check the event type: login attempt, device access, or other suspicious activity.
- Review the source IP and affected device ID.
- Check whether access was successful or failed.
- Prioritize events marked High or Critical.
- Record actions taken in the incident record or team notes, depending on whether the MVP or full system is being used.

### Proposed Full-System Incident Handling

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Select a high or critical alert. | Alert details are opened for review. |
| 2 | Create or update an incident record. | The alert is associated with an investigation. |
| 3 | Assign an analyst or response owner. | Accountability is established. |
| 4 | Add investigation notes and status updates. | Response history is preserved. |
| 5 | Close the incident when resolved and document the outcome. | Leadership can review response quality and trends. |

> **MVP Training Note:** The current GitHub prototype focuses on event display rather than full incident ticket handling. Analysts should describe incident assignment and notes as proposed full-system workflow unless those features are later implemented.

---

## 4. Quick Start Guide: IT Administrator / System Maintainer

This guide is for administrators responsible for maintaining the application, database, and local demonstration environment. It focuses on the simplified MVP while also noting future maintenance needs for the proposed full system.

### Administrator Responsibilities

- Maintain the Python/Flask application environment.
- Maintain the MySQL database and verify required tables exist.
- Apply updates and dependency changes in a test environment before demonstration or production use.
- Protect credentials and never commit real passwords to GitHub or shared documentation.
- Back up database records and verify recovery steps.
- Review simulated alert rules and adjust thresholds as needed.

### MVP Environment Checklist

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Install Python, MySQL Server, and MySQL Workbench on the local machine. | Required platform tools are available. |
| 2 | Open and execute `schema.sql` in MySQL Workbench. | The `sentinel_db` database and `event_logs` table are created. |
| 3 | Update local database credentials in the configuration block or environment variables. | The Flask app and simulation script can connect to MySQL. |
| 4 | Install Python packages such as Flask and `mysql-connector-python`. | Required Python dependencies are available. |
| 5 | Run `app.py` and confirm the dashboard opens locally. | The web application is reachable from the browser. |
| 6 | Run `simulated_attack.py` and verify a new event appears. | Database insertion and dashboard retrieval are working. |

### Database Maintenance Guidance

- Index commonly searched fields as the dataset grows, especially timestamp, severity, source IP, device ID, and status fields.
- Schedule routine backups of the MySQL database and test restore procedures.
- Use least-privilege database accounts for application access.
- Do not store plaintext passwords in the database or source code.
- Archive older event logs if dashboard performance begins to slow.
- Document schema changes before applying them.

> **Security Reminder:** If a real database password was ever committed to GitHub, treat it as exposed and rotate it immediately. Use placeholders or environment variables for local setup instructions.

---

## 5. Quick Start Guide: Prototype Demonstration Operator

This guide is for the team member running the final demonstration. It explains how to show the functional MVP workflow clearly without overstating the prototype scope.

### Demo Goal

Demonstrate the core monitoring workflow: a simulated security event is generated, stored in MySQL, retrieved by the Flask backend, and displayed on the dashboard.

### Demo Steps

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Open MySQL Workbench and confirm `sentinel_db` exists. | Database is ready for the demo. |
| 2 | Confirm the `event_logs` table exists and is empty or contains test data. | The operator knows what should appear during the demo. |
| 3 | Open a terminal in the project folder and run `python app.py`. | The Flask backend starts successfully. |
| 4 | Open `http://127.0.0.1:5000` in a browser. | The dashboard loads. |
| 5 | Open a second terminal and run `python simulated_attack.py`. | A simulated critical event is inserted into MySQL. |
| 6 | Watch the dashboard refresh and display the new event. | The MVP workflow is confirmed live. |

### Suggested Demo Narration

The functional prototype demonstrates the heart of the Sentinel Portal. A Python script simulates suspicious activity, MySQL stores the event, Flask retrieves the latest records through the backend, and the dashboard displays the result for analyst review. This proves the event monitoring workflow without requiring access to a live hospital network. The larger ERD and full system design show how the prototype could later expand into users, roles, incident tracking, analyst notes, and live security feeds.

---

## 6. Severity Levels and Response Expectations

| Severity | Meaning | Example | Expected Response |
|---|---|---|---|
| Low | Informational or low-risk event | Normal successful login | Monitor only; no immediate action. |
| Medium | Unusual but not confirmed malicious | Login from unfamiliar workstation | Review details and watch for repeated behavior. |
| High | Likely suspicious activity | Multiple failed logins from same source | Investigate and notify security lead if pattern continues. |
| Critical | Immediate security concern | Possible brute-force or ransomware-like event | Escalate immediately and begin incident response procedures. |

---

## 7. Troubleshooting and Escalation

| Issue | Likely Cause | Recommended Action |
|---|---|---|
| Dashboard does not load | Flask backend is not running or wrong URL is used | Run `python app.py` and open `http://127.0.0.1:5000`. |
| Dashboard loads but no events appear | No simulated event has been generated or database connection failed | Run `simulated_attack.py` and check `app.py` database credentials. |
| Database connection error | Incorrect MySQL password, server not running, or database missing | Start MySQL, verify credentials, and execute `schema.sql`. |
| Event appears in database but not dashboard | API route or browser refresh issue | Check `/api/alerts` and reload the dashboard. |
| Unexpected data appears | Old test records remain in `event_logs` | Clear test data or document that prior events are historical demo records. |

### Escalation Path

- General staff report suspicious activity to IT/security staff or the help desk.
- Security analysts escalate High and Critical events to the security lead or incident response owner.
- IT administrators escalate application, database, or hosting failures to the system maintainer.
- For the capstone demonstration, unresolved technical issues should be documented and explained as MVP limitations rather than hidden.

---

## 8. Training Completion Checklist

| Task | Completed | Notes |
|---|:---:|---|
| General staff understand MFA safety and credential-sharing risks. | [ ] |  |
| General staff know how to report suspicious activity or missing badges/cards. | [ ] |  |
| Security analysts understand dashboard severity levels and event review steps. | [ ] |  |
| Security analysts understand the proposed full incident workflow. | [ ] |  |
| IT administrators can run the local MVP demonstration environment. | [ ] |  |
| IT administrators understand database backup, indexing, and credential handling expectations. | [ ] |  |
| Demo operator can successfully run `app.py` and `simulated_attack.py`. | [ ] |  |
| Team can explain implemented MVP features versus proposed full-system features. | [ ] |  |

