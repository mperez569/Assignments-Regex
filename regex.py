#1. Python Regular Expressions Deep Dive
#Task 1:
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(pattern, text)
print(emails)
