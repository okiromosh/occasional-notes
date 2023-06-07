"""
This is a script to test sockets
Most of all this happens in the browsers automatically

"""

import socket

# Create a instance of socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Initiate the instance
my_socket.connect(('data.pr4e.org', 80))

# Create a command/task
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()  # \r -return | \n -newline
# Sends the given command through the socket instance
my_socket.send(cmd)

while True:
    # Create a variable to receive the data  from my_socket given command/task
    data = my_socket.recv(512)  # up to the next 512 characters
    if len(data) < 1:  # if my_socket is closed thus receiving <1 data (0) happens if the doc doesnt exist
        break          # stop the script
    print(data.decode(), end=" ")   # otherwise print the decoded data(from UT-8 to UNICODE) and end with a space

my_socket.close()   # Closes the socket



