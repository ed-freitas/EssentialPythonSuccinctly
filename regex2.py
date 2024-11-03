import  re

text = "Call us at +1-800-555-1234 or +1-800-555-5678."

# Define a pattern for phone numbers
phone_pattern = r"\+1-\d{3}-\d{3}-\d{4}"

# Find all phone numbers in the text
matches = re.findall(phone_pattern, text)

print("Found phone numbers:", matches)
