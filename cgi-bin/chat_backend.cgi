#!/usr/bin/python2

import cgi,cgitb,os,time,subprocess,commands,socket

cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
ip_add=web.getvalue('ip')
person=web.getvalue('person')
x=6001


	print os.system(s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM))

if(person=="sender")
	while  True:
	print os.system(data=raw_input("type your message :  "))
        #  it will send data to receiver as well as create own socket (own ip and any random port)
	print os.system(s.sendto(data,(rec_ip,rec_port))  )
	#  this is for receiving from  sender 
	print os.system(print s.recvfrom(10)  )
