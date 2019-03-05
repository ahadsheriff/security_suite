# security_suite
A collection of audit and penetration testing scripts that can be used for cyber security purposes. 

# audit_suite
This directory contains a collection of scripts which are intended for on-site asset discovery. All the scripts contained in this package can be run on a Windows 10 machine with powershell, bash, ubuntu, and python.

DNSenum
* A DNS enumeration tool

OSClassify
* A ICMP based OS detection tool

Ping
* A ping sweep tool

PortScan
* A port scanning tool

SSHScan
    - A brute force SSH login scanning tool
    
# pentest_suite
This directory contains a collection of scripts which are intended for offensive security purposes.

Email Crawler
* A program that crawls a website and recursively checks links to scrape all relevant email addresses

Email Harvester
* A program that uses "the Harvester" tool to gather emails, subdomains, hosts, employee names, open ports and banners from different public sources

Email Regex
* Scrapes a web page for email addresses

Website Mapper
* Crawls a website and recursively checks links to map all internal and external links

Link Finder
* Uses BeautifulSoup to find all URL's in a webpage

Wordlist Maker
* Creates a word-list from a given website using BeautifulSoup.

Chroot Break
* Code that attempts to break out out of a Linux Chroot jail

Netcat Port Scanner
* Simple script that scans ports on a target machine using netcat 
