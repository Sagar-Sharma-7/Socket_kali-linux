import socket
import sys

try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created.")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

port = 80
try: 
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror: 
    print("There was an error resolving the host")
    sys.exit() 

mySocket.connect((host_ip, port))
print("The socket has successfully connect to google on port == %s" % (host_ip))
