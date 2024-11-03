import re

text = "Contact us at support@example.com or sales@example.com."

# Pattern for emails
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

# Substitute emails with a placeholder
masked_text = re.sub(email_pattern, "[hidden email]", text)

print("Text with emails masked:", masked_text)
