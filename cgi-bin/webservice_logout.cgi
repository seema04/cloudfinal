#!/usr/bin/python2

import  cgi,cgitb,os,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""


conn=mysql.connect(user='root', password='seema', host='localhost', database='cloud')

sql=conn.cursor()

sql.execute("SELECT username from loggeduser")

res1=sql.fetchall()

uname=[]
for i in res1:
	uname.append(json.dumps(i).strip('[""]'))

var1='''<!DOCTYPE html>
      <html>
      <head>
       <link href="../login_backendstyle.css" rel="stylesheet" type="text/css">
       </head>
      <body>
         <h3>Bye, '''

print var1
print uname[0]

conn=mysql.connect(user='root', password='seema', host='localhost', database='cloud')
sql=conn.cursor()
sql.execute("DELETE from loggeduser")
conn.commit()


var2='''</h3>
		<h4> You have been logged out! </h4>
         </body>
         </html>
         '''

print var2