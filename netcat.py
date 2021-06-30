import socket
import optparse
import shlex
import sys

class compSystem(self, target, port, data=None):
	self.target = target
	self.port = port
	self.data = data
	self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	def run(self):
		self.sendCommand()

	def sendCommand(self):
		self.socket.connect((self.target, self.port))
		if self.data is not None:
			self.socket.send(self.data)
		try:
			while True:
				data_size = 1
				response = ''
				while True:
					data = self.socket.recv(4096)
					response += data.decode()
					data_size = len(data)
					if data_size < 4096:
						break

					if response:
						print(response)
						data = input('>> ')
						buffer += '\n'

		except:
			print('[-] Connection Terminated')
			self.socket.close()
			sys.exit()

	def handle(self, client):
		if self


def executeCMD(command):
	command = command.strip()
	if command == '':
		return
	return subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT).decode()

def main():
	command = optparse.OptionParser()

if __name__ == '__main__':
	main()
