#!/usr/bin/python2
import commands
commands.getoutput("mkdir /mnt/work1")
commands.getoutput("mount 192.168.1.4:/share_info/work1 /mnt/work1")
commands.getoutput("chmod 777 /mnt/work1")
