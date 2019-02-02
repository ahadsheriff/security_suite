"""
Python script to scrape a web page for all email addresses
"""

from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
import re

url = "http://www.rit.edu/gccis/computingsecurity/people-categories/faculty"

# a set of crawled emails
emails = set()

# get url's content
print("Processing %s" % url)
response = requests.get(url)

# extract all email addresses and add them into the resulting set
new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
emails.update(new_emails)

print(emails)
