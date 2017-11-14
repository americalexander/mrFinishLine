import subprocess
from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902

cmdGen = cmdgen.CommandGenerator()

#Controller class
class Controller:
	exe = None
	isRed = False
	countdownTimer = False
	ip = "127.0.0.1"
	port = 501
	def __init__(self):
		#start controller
		self.exe = subprocess.Popen(["./controller/asc3.exe"],cwd="./controller/")
	
	def kill(self):
		self.exe.terminate()
	
	def snmpGet(self, oid):
		## read value from controller
		errorIndication, _, _, varBinds = cmdGen.getCmd(
			cmdgen.CommunityData('public', mpModel=0),
			cmdgen.UdpTransportTarget((self.ip, self.port)),
			cmdgen.MibVariable(oid)
		)
		if errorIndication != None:
			raise errorIndication
		else:
			return varBinds[0][1]
	
	def snmpSet(self, oid, value):
		## write value to controller
		while True:
			errorIndication, _, _, varBinds = cmdGen.setCmd(
				cmdgen.CommunityData('public', mpModel=0),
				cmdgen.UdpTransportTarget((self.ip, self.port)),
				(oid,value)
			)
			if errorIndication != None:
				raise errorIndication
			else:
				if snmpGet(self.ip,self.port,oid)[0][1] == value:
					return varBinds[0][1]
					
	def updateStatus(self, phase):
		oid = "1.3.6.1.4.1.1206.4.2.1.1.4.1.2.1"
		status = self.snmpGet(oid)
		isRed = bool(int(bin(status)[10-phase]))
		if isRed != self.isRed:
			print("changed")
			self.isRed = isRed
			
	#Manual oid: 1.3.6.1.4.1.1206.4.2.1.4.1.0
	#Phase call oid: 1.3.6.1.4.1.1206.4.2.1.1.5.1.6.1
		#bitwise call to each phase