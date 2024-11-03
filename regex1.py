import re

# Sample text
text = "Contact us at support@example.com for more information."

# Define a pattern for an email
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

# Search for the pattern in the text
match = re.search(email_pattern, text)

if match:
    print("Found email:", match.group())
else:
    print("No email found.")
