import ipaddress
import re
import time
import tlntlib
from .cfg import *

class cisco:
	'''the class describes cisco access
		tln = cisco.telnet(host,user,password)
		iproucheck = tln.check_iprou(iprou)
		makeiprou = tln.make_iprou(iprou)
		showtime = tln.show_clock()
	'''
	def __init__(self,host,username,password):
	 	self.host = host
	 	self.username = username
	 	self.password = password
	 	remote = tlntlib.telnet(self.host,self.username,self.password)
	 	self.remote = remote

	def telnet(self):
		try:			
			self.remote.connect()		
		except:
			print("can't telnet!") 

	def sendcmd(self,cmd):		
		self.remote.connect()
		logger.debug(f'{self.host} : Connected')
		result = self.remote.cmd(cmd)
		if result:
			logger.warning(f'{self.host} : Answered: {result}')
		self.remote.disconnect()
		logger.debug(f'{self.host} : Disconnected')
		reply = result.split('\n')
	#	return reply[1]
		return result

	def sendconfigcmd(self,cmdlist):
		result = []
		self.remote.connect()
		self.remote.cmd("config terminal")
		for c in cmdlist:
			answer = self.remote.cmd(c)
			result.append(answer)
		self.remote.cmd("end")
		self.remote.disconnect()
		return result

	def showclock(self):
	#returns /system identity print
		command = "show clock"
		result = self.sendcmd(command)
		return result

	def showrou(self,ip):
	#returns /system identity print
		command = "show ip route "+str(ip)
		result = self.sendcmd(command)
		return result


	def execCommand(self, cmd):
		result = tlnt.execCommand(self, cmd)
		return result

	def splitcmd(self,s,line):
		''' splits cmd to list'''
		result = s.split('\n')
		return result[line].split()

	def shiprou(self,ip):
		command = "show ip route "+str(ip)
		iproute = self.remote.cmd(command)
		routestr = iproute.split('\n')
		route = routestr[1].split()
		try:
			rnet = ipaddress.ip_network(route[3])
			if rnet.num_addresses > 255:
				return True
			else:
				return False
		except:
			print(mass[i]," not in route table")
			return False

	def lookfor(self,cmd,expected):
		''' checks command with attribute and returns result if answer True'''		
		answer = str(self.remote.cmd(cmd))
		if expected in answer:
			return True
		else:
			return False

	def vlancheck(self,vlan):
		''' checks if vlan is ocupied '''
		vlanstr = str(vlan)
		command = 'show vlan id ' + vlanstr
		if self.lookfor(command,'not found'):
			return True
		else:
			return False

	def MACforvlan(self,vlan):
		''' checks if macs in dynamic-table for the vlan'''
		vlanstr = str(vlan)
		command = 'sh mac-address-table dynamic vlan '+vlanstr
		if self.lookfor(command,'No entries present'):
			return False
		else:
			return True

	def getVLANports(self,vlan):
		''' gets ports of vlan'''
		vlanstr = str(vlan)
		command = 'show vlan id ' + vlanstr
		answer = str(self.remote.cmd(command))
		if 'VLAN' in answer and 'not found' not in answer:
			vlanports = self.splitcmd(answer,4)
			return vlanports[3:]
		else:
			return False



################JUNK
	def checkNETrou(self,subnet):
		'''checks if all ip from subnet was routed already if it is - Returns cisco output'''	
		try:
			subnet = ipaddress.ip_network(subnet)
		except:
			print(subnet," it looks like  not a subnet :(")
			return False
		self.telnet()
		counter = 0
		for ip in subnet:
			if self.shiprou(ip):
				counter += 1
		if counter != subnet.num_addresses:
			return False
		else:
			return True


	def __del__(self):
		if self.remote:
			self.remote.disconnect()
			self.remote = None
