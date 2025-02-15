#服务器端代码编写
from socket import socket, AF_INET,SOCK_STREAM#VS import xx from xx, don't need to socket.socket
from time import localtime

#1 Internet之间的进程通信 2表示TCP协议编程

#create object
server_socket=socket(AF_INET,SOCK_STREAM)
#bind ip and port
ip='127.0.0.1'#127.0.0.1
port=8888#range of port
server_socket.bind((ip,port))
#listen for monitoring
server_socket.listen(5)
print('server has started')
#wait for connection from clients
client_socket,client_addr=server_socket.accept()#unpacked assignment
#receive
data=client_socket.recv(1024)#how many
print('the data from client:',data.decode('utf-8'))

server_socket.close()

