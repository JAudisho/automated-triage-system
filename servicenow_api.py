import logging

def create_incident(description, priority, category):
    # Simulate ServiceNow API call
    logging.info("Creating incident in ServiceNow...")
    logging.info(f"Description: {description}")
    logging.info(f"Priority: {priority}")
    logging.info(f"Category: {category}")
    # Example: requests.post("https://instance.service-now.com/api/...", ...)
