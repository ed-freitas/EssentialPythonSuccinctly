import re

# Define a date pattern
date_pattern = r"^\d{4}-\d{2}-\d{2}$"

# Sample date inputs
dates = ["2024-10-29", "29-10-2024", "2024/10/29"]

for date in dates:
    if re.match(date_pattern, date):
        print(f"{date} is a valid date format.")
    else:
        print(f"{date} is an invalid date format.")
