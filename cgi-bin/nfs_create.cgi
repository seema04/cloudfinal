#!/usr/bin/python2

import  cgi,cgitb,os,json
import mysql.connector as mysql

cgitb.enable()

print  "Content-type:text/html"
print  ""
conn=mysql.connect(user='root', password='seema', host='localhost', database='aws')

sql=conn.cursor()
sql.execute('select user_name from currentuser')
res=sql.fetchall()
user=[]
for i in res:
	user.append(json.dumps(i).strip('[""]'))

sql.execute('select storage_name from nfs where user_name=%s',(user[0],))
result=sql.fetchall()

nfs=[]
for i in result:
	nfs.append(json.dumps(i).strip('[""]'))


var1='''
<!DOCTYPE html>
<html>
<body>
<form action="" method=POST>
<p>Your existing storages:</p>
'''
print var1
for i in nfs:
	print '<input ="" value=','"',i,'">',i
var2='''
<input type="submit">
</form>
</body>
</html>
'''
print var2