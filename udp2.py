from socket import socket,AF_INET, SOCK_STREAM,SOCK_DGRAM

def connect_to_server():
    try:
        # 创建一个 TCP 套接字
        s = socket(AF_INET,SOCK_STREAM)
        # 尝试连接到服务器，这里假设服务器 IP 是 127.0.0.1，端口是 8080
        s.connect(('127.0.0.1', 8080))
        print("连接成功")
    except ConnectionRefusedError as e:
        print(f"连接失败，错误信息：{e}")
        # 这里可以添加相应的处理逻辑，如重新尝试连接或修改配置
    finally:
        s.close()
def main():
    # 创建一个 UDP 套接字，使用 IPv4 协议族和数据报套接字类型
    socket_re = socket(AF_INET,SOCK_DGRAM)
    # 绑定到本地地址和端口，确保端口没有被其他程序占用
    socket_re.bind(('127.0.0.1', 8088))
    try:
        # 接收数据和发送方地址，使用 recvfrom 函数，1024 是缓冲区大小
        recv_data, adre = socket_re.recvfrom(1024)
        print(recv_data.decode(), adre)
    except OSError as e:
        print(f"Error occurred: {e}")
    finally:
        socket_re.close()


if __name__ == "__main__":
    main()
if __name__ == "__main__":
    connect_to_server()
#create
socket_re=socket(AF_INET, SOCK_STREAM)
while True:
    recv_data,adre=socket_re.recvfrom(1024)#bufsize buffer
    print('the client say:',recv_data.decode())
    if recv_data.decode()=='bye':
        break
    else:
        data=input("reply:")
    socket_re.sendto(data.encode(),('localhost',8888))#adre is ok
socket_re.close()

