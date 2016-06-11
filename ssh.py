#!/usr/bin/python

###this is a script to ssh to cisco devices

import paramiko
import os
import sys

class Device_ssh(object):
	def __init__(self,ip,username,password):
		self.ip = ip
		self.user = username
		self.password = password

	def connect_device(self):
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(self.ip,username = self.user,password=self.password)

	def rundevicecmd(self,cmd):
		(iin,out,err) = self.ssh.exec_command(cmd)
		if out:
			for line in out.readlines():
				print line
			else:
				print "Error: ",err
			self.ssh.close()





ip = raw_input("give ip: ")
username = raw_input("give username: ")
password = raw_input("give pass: ")
cmd = raw_input("give command: ")
device = Device_ssh(ip,username,password)
device.connect_device()
device.rundevicecmd(cmd)
