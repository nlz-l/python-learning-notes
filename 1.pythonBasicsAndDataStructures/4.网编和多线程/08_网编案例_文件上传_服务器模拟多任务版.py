
import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.20.10.2',10086))
server_socket.listen(5)
count = 0
while True:
    try:
        count += 1
        accept_socket,client_info = server_socket.accept()
        with open('./data/picture' + str(count) + '.jpg','wb') as dest_f:
            while True:
                bys = accept_socket.recv(8192)

                #无数据,结束即可
                if len(bys) == 0:
                    break
                dest_f.write(bys)

    #accept_socket.send("文件上传成功".encode("utf-8"))

        accept_socket.close()
    except:
        pass
