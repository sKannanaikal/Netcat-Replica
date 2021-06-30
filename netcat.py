import socket
import optparse

def connect(target, port):
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.connect(target, port)

def main():
	command = optparse.OptionParser()

if __name__ == '__main__':
	main()
