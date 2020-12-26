import socket

def get(url):
	ip = socket.gethostbyname(url)
	return ip
