# Automated IT Ticket Triage System

A Python-based tool that integrates natural language processing with the ServiceNow API to classify and escalate IT tickets automatically based on urgency and keywords.

## 🔍 Overview

This project was built to automate triage for common IT issues such as VPN lockouts, account compromise attempts, and password resets. By combining basic NLP and mock ServiceNow API calls, the system simulates how real incidents could be flagged and escalated in a production environment.

## ⚙️ Features

- Built an NLP-driven classification tool to flag high-risk incidents based on ticket descriptions
- Integrated with the ServiceNow API to simulate real-time incident creation and escalation
- Auto-categorizes incidents into categories like "Access Issues", "Account Management", etc.
- Sample incidents include VPN connection problems, account lockouts, and more
- Designed with modularity to plug into actual ticketing systems in future

## 🧠 Tech Stack

- Python 3.10+
- NLP via basic string matching (expandable to spaCy/NLTK)
- Mocked ServiceNow API calls using `requests`
- JSON for data input and configuration

## 📁 Structure

- `main.py` – Entry point – loads and classifies tickets
- `nlp_classifier.py` – NLP logic for ticket classification
- `servicenow_api.py` – Mocks ticket creation with ServiceNow API
- `sample_tickets.json` – Sample data to triage
- `config.json` – Placeholder for credentials
- `requirements.txt` – Python dependencies

## 🚀 Sample Run

$ python main.py

[+] Creating incident:
Description: User unable to connect via VPN
Priority: High
Category: Access Issues


## 🔐 Note

This is a demo project. No real credentials or production API calls are made.