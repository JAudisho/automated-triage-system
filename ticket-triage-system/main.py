import json
import logging
from nlp_classifier import classify_ticket
from servicenow_api import create_incident

logging.basicConfig(level=logging.INFO)

def load_tickets():
    with open('sample_tickets.json') as f:
        return json.load(f)

def main():
    tickets = load_tickets()
    for ticket in tickets:
        priority, category = classify_ticket(ticket["description"])
        logging.info(f"Classified ticket as Priority: {priority}, Category: {category}")
        create_incident(ticket["description"], priority, category)

if __name__ == "__main__":
    main()