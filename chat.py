#coding:utf-8
import threading
import wx
from socket import socket, AF_INET, SOCK_STREAM


class kiki(wx.Frame):
    def __init__(self, client_name):
        wx.Frame.__init__(self, None, id=1001, title=client_name + 's interface',
                          pos=wx.DefaultPosition, size=(500, 500))
        panel = wx.Panel(self)
        box_sizer = wx.BoxSizer(wx.VERTICAL)

        # 按钮区域 1
        button_grid_sizer1 = wx.FlexGridSizer(wx.HSCROLL)
        connect_button = wx.Button(panel, size=(100, 30), label="connect")
        disconnect_button = wx.Button(panel, size=(100, 30), label="disconnect")
        button_grid_sizer1.Add(connect_button, 1, wx.TOP | wx.RIGHT, 5)
        button_grid_sizer1.Add(disconnect_button, 1, wx.TOP | wx.LEFT, 5)
        box_sizer.Add(button_grid_sizer1, 1, wx.ALIGN_CENTRE | wx.ALL, 10)

        # 显示消息的文本框
        self.show_text_ctrl = wx.TextCtrl(panel, size=(400, 300),  # 增大宽度
                                          style=wx.TE_MULTILINE | wx.TE_READONLY)
        box_sizer.Add(self.show_text_ctrl, 1, wx.ALL | wx.EXPAND, 10)

        # 输入消息的文本框
        self.input_text_ctrl = wx.TextCtrl(panel, size=(400, 50))  # 增大宽度
        box_sizer.Add(self.input_text_ctrl, 0, wx.ALL | wx.EXPAND, 10)

        # 按钮区域 2
        button_grid_sizer2 = wx.FlexGridSizer(wx.HSCROLL)
        reset_button = wx.Button(panel, size=(100, 30), label="reset")
        send_button = wx.Button(panel, size=(100, 30), label="send")
        button_grid_sizer2.Add(reset_button, 1, wx.TOP | wx.RIGHT, 5)
        button_grid_sizer2.Add(send_button, 1, wx.TOP | wx.LEFT, 5)
        box_sizer.Add(button_grid_sizer2, 0, wx.ALIGN_CENTRE | wx.ALL, 10)

        panel.SetSizer(box_sizer)

        # 绑定按钮事件
        self.Bind(wx.EVT_BUTTON, self.connect_to_server, connect_button)
        self.Bind(wx.EVT_BUTTON, self.disconnect_from_server, disconnect_button)
        self.Bind(wx.EVT_BUTTON, self.reset_input, reset_button)
        self.Bind(wx.EVT_BUTTON, self.send_message, send_button)

        # 实例属性
        self.client_name = client_name
        self.isConnected = False
        self.client_socket = None

    def connect_to_server(self, event):
        if not self.isConnected:
            server_host_port = ('127.0.0.1', 8888)
            self.client_socket = socket(AF_INET, SOCK_STREAM)
            try:
                self.client_socket.connect(server_host_port)
                self.isConnected = True
                # 发送客户端名称
                self.client_socket.send(self.client_name.encode('utf-8'))
                print(f"客户端 {self.client_name} 已连接到服务器")
                # 启动接收消息的线程
                client_thread = threading.Thread(target=self.recv_data)
                client_thread.daemon = True
                client_thread.start()
            except ConnectionRefusedError:
                print("无法连接到服务器，请检查服务器是否运行。")

    def disconnect_from_server(self, event):
        if self.isConnected:
            try:
                self.client_socket.send('disconnect'.encode('utf-8'))
                self.client_socket.close()
                self.isConnected = False
                print(f"客户端 {self.client_name} 已断开连接")
            except Exception as e:
                print(f"断开连接时发生错误: {e}")

    def reset_input(self, event):
        self.input_text_ctrl.SetValue('')

    def send_message(self, event):
        if self.isConnected:
            message = self.input_text_ctrl.GetValue()
            if message:
                try:
                    self.client_socket.send(message.encode('utf-8'))
                    self.input_text_ctrl.SetValue('')
                except Exception as e:
                    print(f"发送消息时发生错误: {e}")

    def recv_data(self):
        while self.isConnected:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                wx.CallAfter(self.show_text_ctrl.AppendText, '$' * 30 + '\n' + message + '\n')
            except Exception as e:
                print(f"接收数据时发生错误: {e}")
                break


if __name__ == '__main__':
    app = wx.App()
    name = input('please input your name:')
    client = kiki(name)
    client.Show()
    app.MainLoop()

