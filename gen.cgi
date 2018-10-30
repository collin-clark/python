#! /Python/python

import cgi, cgitb
cgitb.enable()

def htmlTop():
	print("""Content-type:text/html\r\n\r\n
				<!DOCTYPE html>
				<html lang="en">
					<head>
						<meta charset="utf-8"/>
						<title> Object & ACL Generator </title>
					</head>
					<body><font face="consolas, arial, tahoma" color="black">""")

def htmlTail():
	print("""</body>
		</font>
		</html>""")					
		
if __name__ == "__main__":
	try:
		htmlTop()
		
		form = cgi.FieldStorage()
		dst = form.getvalue('dst')
		dst_desc = form.getvalue('dst_desc')
		src = form.getvalue('src')
		src_desc = form.getvalue('src_desc')
		port = form.getvalue('port')
		newline = """<br>"""
		
		if form.getvalue('src_mask'):
			src_mask = form.getvalue('src_mask')
		else:
			src_mask = "0.0.0.0"
		if form.getvalue('dst_mask'):
			dst_mask = form.getvalue('dst_mask')
		else:
			dst_mask = "0.0.0.0"
		
		src_cidr = sum([bin(int(x)).count("1") for x in src_mask.split(".")])
		dst_cidr = sum([bin(int(x)).count("1") for x in dst_mask.split(".")])
		
		if form.getvalue('logging'):
			logging_flag = "logging"
		else:
			logging_flag = ""
		
		if form.getvalue('inactive'):
			inactive_flag = "inactive"
		else:
			inactive_flag = ""

		if form.getvalue('protocol'):
			protocol = form.getvalue('protocol')
		else:
			protocol = "--ERROR--"
			
		#print("Logging is: " + (logging_flag))
		#print(newline)
		#print("ACL is: " + (inactive_flag))
		print("<h3> !--Source </h3>")
		print("object network " + str(src) + "_" + str(src_cidr))
		print(newline)
		print("network " + str(src) + " " + str(src_mask))
		print(newline)
		print("description " + str(src_desc))
		
		print("<h3> !--Destination </h3>")
		print("object network " + str(dst) + "_" + str(dst_cidr))
		print(newline)
		print("	network " + str(dst) + " " + str(dst_mask))
		print(newline)
		print("description " + str(dst_desc))
		print(newline)
		print("<h3> !--ACE </h3>")
		print("access-list inside_access_in permit " + str(protocol) + " " + str(src) + " " + str(src_mask) + " " + str(dst) + " " + str(dst_mask) + " eq " + str(port) + " " + (logging_flag) + " " + (inactive_flag))
		
		htmlTail()
	except:
		cgi.print_exception()
			