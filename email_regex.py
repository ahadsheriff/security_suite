"""
Script to scrape a website for all email addresses
"""

import code
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re