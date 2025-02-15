#coding:utf-8
import threading
import wx
from socket import socket, AF_INET, SOCK_STREAM


class server(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=1002, title='the server', pos=wx.DefaultPosition, size=(600, 600))
        pl = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        # 按钮区域
        fgz1 = wx.FlexGridSizer(wx.HSCROLL)
        bon1 = wx.Button(pl, size=(200, 50), label="start")
        bon2 = wx.Button(pl, size=(200, 50), label="stop")
        bon3 = wx.Button(pl, size=(200, 50), label="save")
        fgz1.Add(bon1, 1, wx.TOP | wx.RIGHT, 5)
        fgz1.Add(bon2, 1, wx.TOP, 5)
        fgz1.Add(bon3, 1, wx.TOP | wx.LEFT, 5)
        box.Add(fgz1, 1, wx.ALIGN_CENTRE)

        # 显示消息的文本框
        self.show = wx.TextCtrl(pl, size=(500, 500), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show, 1,wx.ALL | wx.EXPAND, 10)

        pl.SetSizer(box)

        # 服务器状态
        self.isOn = False
        # 服务器地址和端口
        self.host_port = ('', 8888)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(self.host_port)
        self.server_socket.listen(5)

        # 绑定按钮事件
        self.Bind(wx.EVT_BUTTON, self.start_server, bon1)
        self.Bind(wx.EVT_BUTTON, self.stop_server, bon2)

        # 存储客户端线程的字典
        self.session_thread_dict = {}

    def start_server(self, event):
        if not self.isOn:
            self.isOn = True
            # 创建主线程来处理客户端连接
            main_thread = threading.Thread(target=self.do_work)
            main_thread.daemon = True
            main_thread.start()
            self.show_message("服务器已启动")

    def stop_server(self, event):
        if self.isOn:
            self.isOn = False
            # 关闭所有客户端连接
            for thread in self.session_thread_dict.values():
                thread.isOn = False
                thread.client_socket.close()
            self.server_socket.close()
            self.show_message("服务器已停止")

    def do_work(self):
        while self.isOn:
            try:
                # 接受客户端连接
                session_socket, client_addr = self.server_socket.accept()
                user_name = session_socket.recv(1024).decode('utf-8')
                # 创建一个客户端线程
                session_thread = Session_Thread(session_socket, user_name, self)
                self.session_thread_dict[user_name] = session_thread
                session_thread.start()
                self.show_message(f"客户端 {user_name} 已连接")
            except Exception as e:
                if self.isOn:
                    self.show_message(f"接受客户端连接时发生错误: {e}")

    def show_message(self, message):
        wx.CallAfter(self.show.AppendText, message + '\n')

    def broadcast_message(self, sender, message):
        full_message = f"{sender}: {message}"
        for user_name, thread in self.session_thread_dict.items():
            if user_name != sender:
                try:
                    thread.client_socket.send(full_message.encode('utf-8'))
                except Exception as e:
                    self.show_message(f"向 {user_name} 广播消息时发生错误: {e}")


class Session_Thread(threading.Thread):
    def __init__(self, client_socket, user_name, server):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.user_name = user_name
        self.server = server
        self.isOn = True

    def run(self):
        while self.isOn:
            try:
                data = self.client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                if data == 'disconnect':
                    self.isOn = False
                    self.server.show_message(f"客户端 {self.user_name} 已断开连接")
                else:
                    self.server.show_message(f"{self.user_name}: {data}")
                    self.server.broadcast_message(self.user_name, data)
            except Exception as e:
                self.isOn = False
                self.server.show_message(f"处理 {self.user_name} 的消息时发生错误: {e}")
        self.client_socket.close()
        del self.server.session_thread_dict[self.user_name]


if __name__ == '__main__':
    app = wx.App()
    server_instance = server()
    server_instance.Show()
    app.MainLoop()


