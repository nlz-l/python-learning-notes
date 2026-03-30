import socket

# Address Family 地址族 即IPV4 还是 IPV6 默认值AF_INET(ipv4) AF_INET6(ipv6)
# Socket Type Socket类型 即TCP 还是 UDP 默认值 SOCK_STREAM(TCP) SOCK_DGRAM(UDP)

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)
