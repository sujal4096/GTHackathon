import re

def mask_sensitive_data(text: str) -> str:
    """
    Replaces email addresses and phone numbers with placeholders.
    """
    # Regex for email
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    text = re.sub(email_pattern, '[EMAIL_REDACTED]', text)

    # Regex for phone numbers (simple 10 digit or standard formats)
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    text = re.sub(phone_pattern, '[PHONE_REDACTED]', text)

    return text