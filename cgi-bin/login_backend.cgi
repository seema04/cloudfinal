#!/usr/bin/python2

import  cgi,cgitb,os,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""

flag=0

web=cgi.FieldStorage()
d_username=web.getvalue('username')
d_password=web.getvalue('password')
d_username=d_username.strip(' ')
d_password=d_password.strip(' ')

conn=mysql.connect(user='root', password='seema', host='localhost', database='cloud')

sql=conn.cursor()

sql.execute("SELECT username from user where username=%s AND password=%s",(d_username,d_password))

res=sql.fetchall()

#print res,flag

uname=[]
for i in res:
	uname.append(json.dumps(i).strip('[""]'))
	flag=flag+1
	
#print uname[0],flag

var1='''<!DOCTYPE html>
      <html>
      <head>
       <link href="../login_backendstyle.css" rel="stylesheet" type="text/css">
       </head>
      <body>
         <h1>Login Successful!</h1>
         <br>
         '''

var2='''<!DOCTYPE html>
      <html>
      <head>
      <link href="../login_backendstyle.css" rel="stylesheet" type="text/css">
      </head>
      <body>
         <h1>Login Unsuccessful!</h1>
         <br>
         <h2> Check username/password </h2>
         <br>
         <a href="../login.html">click to login again.</a>
      </body>
   </html>'''

if flag>0 :
   
   print var1
   print'<h2>Welcome, '
   print uname[0]
   print'''</h2> <br>
      <a href="../webafterlogin.html">click to access services.</a>
      </body>
      </html>'''

   conn=mysql.connect(user='root', password='seema', host='localhost', database='cloud')
   sql=conn.cursor()
   sql.execute("INSERT INTO loggeduser VALUES (%s)",(uname[0],))
   conn.commit()



else :
   print var2





