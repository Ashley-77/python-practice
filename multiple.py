#interaction you have project2
from socket import socket, AF_INET,SOCK_STREAM
socket_obj=socket(AF_INET,SOCK_STREAM)#socket.SOCK_STREAM not
socket_obj.bind(('127.0.0.1',8888))
socket_obj.listen(8)#max connection number
socket_client,client_addr=socket_obj.accept()
info=socket_client.recv(1024).decode('utf-8')
while info!='bye':
    if info!='':
        print(info,'is what you receive')
    data=input("what do you want to send")
    #server's response
    socket_client.send(data.encode('utf-8'))#client send and recv
    if data=='bye':
        break
    info = socket_client.recv(1024).decode('utf-8')
socket_obj.close()
socket_client.close()