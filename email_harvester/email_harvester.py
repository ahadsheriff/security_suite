import sys
import os, getopt
import subprocess
import re

def main(argv):
	domain = ''
	provider = ''

	try:
		opts, args = getopt.getopt(argv,"hd:p:",["domain=","provider="])
	except getopt.GetoptError:
		print ('test.py -d <domain> -p <provider>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -d <domain> -p <provider>')
			sys.exit()
		elif opt in ("-d", "--domain"):
			domain = arg
		elif opt in ("-p", "--provider"):
			provider = arg
	
	if provider is '':
		print ('Domain file is ', domain)
	else:
		two(domain, provider)


def two(domain, provider):
	print('Argument One:', sys.argv[1])
	print('Argument Two:', sys.argv[2])

	domain = sys.argv[1]
	provider = sys.argv[2]

	cmd = '/usr/bin/theharvester -d ' + domain + ' -b ' + provider

	with open("./outfile.txt", "wb", 0) as out:
		subprocess.run([cmd], stdout=out, check=True, shell=True)

if __name__ == "__main__":
	main(sys.argv[1:])
