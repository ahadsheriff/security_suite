"""
Python script to scrape a web page for all email addresses
"""

import code
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
