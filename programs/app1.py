import socket 
import sys 
HOST =  ""

# You can choose any arbitrary port number
PORT = 8080
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket has been created')

# Let us bind the socket to local host and port
try:
    mySocket.bind((HOST, PORT))
except socket.error as msg:
    print('Binding has failed. Error Code is : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
    
print('Socket bind is complete. Now we can proceed to make itlisten...')

# Server
mySocket.listen(10)
print('Socket is now listening')
# Let the server keep talking with the client
while 1:
# We are waiting to accept a connection - blocking call
    connection, address = mySocket.accept()
    print('Connected with ' + address[0] + ':' +
    str(address[1]))
mySocket.close()