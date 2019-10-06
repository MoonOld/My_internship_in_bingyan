'''   
这是创建UDP服务器的伪代码
ss = socket()                                            #创建服务器socket
ss.bind()                                                #绑定服务器socket 
inf_loop:                                                #服务器的无限循环
    cs = ss.recvfrom()/ss.sendto()                       #服务器的接收/发送 
ss.close()                                               #关闭服务器（不过好像一般用不到
'''
#-*- coding:unicode_escape -*-
from socket import *                                     #引入模块socket和time
from time import ctime      

HOST = ''                                                #主机名取任何可用的（对bind的标识
PORT = 21568                                             #取一个可用端口
BUFSIZ = 4                                               #缓存区规定4字节
ADDR = (HOST, PORT)                                      #服务器地址

UDPSerSock = socket(AF_INET, SOCK_DGRAM)                 #创建服务器的套接字
UDPSerSock.bind(ADDR)                                    #讲地址绑定到套接字

while True:                                              #循环开始
    print('waiting for message...')                      
    data_rcvall = b""                                    #创建一个空的bytes变量来装载接收的数据
    while True:                                          #分包接收数据并连接（或者说pack起来？
        data, addr = UDPSerSock.recvfrom(BUFSIZ)
        data_rcvall += data
        if len(data) < BUFSIZ:
            break                                        #获取客户端消息(完全接收）和地址 
    data_str = data_rcvall.decode("unicode_escape")               #解码消息
    print(data_str)                                      #打印消息（其实是用来debug的）
    data_b_time = '[{}]'.format(ctime())                 #添加时间戳data_b_time
    data_b_tosend = data_b_time + data_str               #拼接字段
    data_b_tosend = data_b_tosend.encode("unicode_escape")        #编码unicode字段
    for i in range(len(data_b_tosend)//4+1):             #再拆分为长度小于等于4的bytes以echo
        if 4*(i+1) < len(data_b_tosend):
            UDPSerSock.sendto(data_b_tosend[4*i:4*i+4],addr)
        else:
            UDPSerSock.sendto(data_b_tosend[4*i:],addr)           
    print('...received from and returned to:',addr)      #打印消息以提示
UDPSerSock.close()                                       #关闭UDP服务器