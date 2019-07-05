#!/usr/bin/python2

import  cgi,cgitb,os,time,subprocess,commands
cgitb.enable()

print  "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
os_name=web.getvalue('os')
os_ram=web.getvalue('ram')
os_cpu=web.getvalue('cpu')
os_hdd=web.getvalue('hdd')

#print  os_name,os_ram,os_cpu,os_hdd

#Now launching an OS:

if  os_name == "RedHat"  :
	#print 'abc'
	print commands.getoutput('sudo virt-install --name '+os_name+' --ram  '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/rhvmdnd.qcow2 --import --noautoconsole &')

elif  os_name ==  "rhel7"  :
	#  a fresh copy 
	
	print  commands.getoutput('sudo  qemu-img   create -f  qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2  /var/lib/libvirt/images/'+os_name+'.qcow2')

	print commands.getoutput('sudo  virt-install  --name '+os_name+' --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/'+os_name+'.qcow2  --import  --noautoconsole --graphics=vnc,listen=192.168.1.5,port=5952,password=redhat')
	
	print os.system('sudo websockify -D --web=/usr/share/novnc 6222 192.168.1.5:5952 ')

	print commands.getoutput('sudo qr "192.168.1.5:6222" > /var/www/html/images/'+os_name+'.png ')

	print '	<a target="_blank" href = ../images/'+os_name+'.png> Click here to access QR code </a>'
