"""
    Simple port scanner using netcat 
"""

import sys
import getopt
import subprocess
import re


def main(argv):
	ip_host = ''
	start_port = ''
	end_port = ''
    
	try:
		opts, args = getopt.getopt(argv, "hi:s:e", ["ip_host=", "start=", "end="])
	except getopt.GetoptError:
		print('test.py -i <ip_host> -s <start_port> -e <end_port>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
		    print('test.py -i <ip_host> -s <start_port> -e <end_port>')
            sys.exit()
		elif opt in ("-i", "--iphost"):
			ip_host = arg
		elif opt in ("-s", "--startport"):
			start_port = arg
        elif opt in ("e", "--endport")
		    end_port = arg

	scanner(ip_host, start_port, end_port)


def scanner(ip_host, start_port, end_port):
    # cast all variables to integers
    ip_host = int(ip_host)
    start_port = int(start_port)
    end_port = int(end_port)
	print('Host IP:', ip_host)
	print('Start Port:', start_port)
    print('End Port:', end_port)

    # run netcat port scanning
	cmd = 'nc -zp 9090 ' + ip_host + ' ' + start_port + '-' + end_port + ' -v'

	print("SCANNING...")

    # write results to a txt file
	with open("./outfile.txt", "wb", 0) as out:
	    subprocess.run([cmd], stdout=out, check=True, shell=True)


if __name__ == "__main__":
	main(sys.argv[1:])
