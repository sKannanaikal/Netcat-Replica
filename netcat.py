import socket
import optparse

class compSystem(self, target, port, data=None):
	self.target = target
	self.port = port
	self.data = data
	self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def run(self):
		if self.cmd_args.wait:
			self.listen()
		else:
			self.send()

	def sendCommand(self):
		self.socket.connect((self.target, self.port))
		if self.buffer is not None:
			self.socket.send(self.data)
		try:
			bas
		except:
			bas


def executeCMD(command):
	command = ''

def main():
	command = optparse.OptionParser()

if __name__ == '__main__':
	main()
