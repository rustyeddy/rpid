import io
import socket
import struct
import cv2

from pprint import pprint
# group = '225.1.1.1'
# addrinfo = socket.getaddrinfo(group, None)[0]

# server_socket = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.bind(('', 8123))

# join the group
# gbin = socket.inet_pton(addrinfo[0], addrinfo[4][0])
# mreq = gbin + struct.pack('=I', socket.INADDR_ANY)
# server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(2)

print("Fixin to open a  a connection")
connection = server_socket.accept()[0].makefile('rb')
pprint(connection)

try:
    while True:

        print("Waiting for incoming packet")

        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        print("Incoming packet it was this long " + str(image_len))
        if not image_len:
            break
            
        #image_stream = io.BytesIO()
        #image_stream.write(connection.read(image_len))
        #image_stream.seek(0)
        #print("Image stream")

        cv2.imshow("Image", connection.read(image_len))
        
        # cv2.imshow("Image", image_stream)

        # Add open CV right here
        # image = Image.open(image_stream)
        # print('Image is %dx%d' % image.size)
        # image.verify()
        # print("Image is verified")
         
finally:

    connection.close()
    server_socket.close()
    
    
        
