#!/usr/bin/python2

import  cgi,cgitb,os,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""


web=cgi.FieldStorage()
d_name=web.getvalue('name')
d_username=web.getvalue('username')
d_email_id=web.getvalue('email_id')
d_password=web.getvalue('password')
d_gender=web.getvalue('gender')


conn=mysql.connect(user='root', password='seema', host='localhost', database='cloud')

sql=conn.cursor()
sql.execute("INSERT INTO user VALUES(%s,%s,%s,%s,%s)",(d_name,d_username,d_email_id,d_password,d_gender))
conn.commit()


var='''<!DOCTYPE html>
<html>
<head>
	<link href="../post_register_style.css" rel="stylesheet" type="text/css">
    <title>logging in</title>
    <h1> Registration Successful. Click below to Login! </h1>
    <a href="../login.html">Login Here</a>
</head>

</html>
'''
print var





conn.close()
