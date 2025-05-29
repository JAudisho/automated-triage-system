def classify_ticket(text):
    text = text.lower()
    if "vpn" in text or "lockout" in text:
        return "High", "Access Issues"
    elif "password reset" in text:
        return "Medium", "Account Management"
    else:
        return "Low", "General"
