'''
clisocket = socket()                        #创建客户端的socket
comm_loop:                                  #通信的循环
    clisocket.sendto()/clisocket.recvfrom() #对话：发送和接收
clisocket.close()                           #关闭客户端socket
'''




from socket import *                                      #import socket的everything

HOST = 'localhost'                                        #主机名（ip
PORT = 21567                                              #端口
BUFSIZ = 4                                                #设置缓冲区大小4字节
ADDR = (HOST,PORT)                                        #地址设定

UDPClientSock = socket(AF_INET, SOCK_DGRAM)               #创建AF_INET族的SOCK_DGRAM的套接字

while True:                                               #发送消息循环
    data = input('>>>')                                   #获取输入信息
    data_b = data.encode("UTF-8")                         #转换信息为UTF-8码
    if not data:                                          #若输入信息为空则停止
        break
    UDPClientSock.sendto(data_b,ADDR)                              #向ADDR地址（服务器）发送data_b数据报
    while True:
        data_b_rcvall = b""                                        #创建了receive_all变量以完全接收消息（大于缓存的）
        data_b_rcv, ADDR = UDPClientSock.recvfrom(BUFSIZ)          #接收信息和地址（ADDR貌似在这里没用了
        data_b_rcvall +=  data_b_rcv                               
        if len(data_b_rcv) < BUFSIZ:
            break
    data_b_rcvall = data_b_rcvall.decode("UTF-8")                  #对data_b解码
    print(data_b_rcvall)                                                  #打印data_b内容

UDPClientSock.close()                                              #关闭客户端socket