#udp once   $sender
from socket import socket,AF_INET, SOCK_STREAM
socket_1=socket(AF_INET,SOCK_STREAM)
ip_port=('127.0.0.1',8888)#tuple
print('ok')
#send to
a=input('what do you want to send')
send_socket=socket_1.sendto(a.encode('gbk'),ip_port)
recv_data,addr=socket_1.recvfrom(1024)
print('received:',recv_data.decode('gbk'))
socket_1.close()