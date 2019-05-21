import io
import socket
import struct
import time
import picamera

class SplitFrames(object):
    def __init__(self, connection):
        self.connection = connection
        self.stream = io.BytesIO()
        self.count = 0

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # Start of new frame; send the old one's length
            # then the data
            size = self.stream.tell()
            if size > 0:
                self.connection.write(struct.pack('<L', size))
                self.connection.flush()
                self.stream.seek(0)
                self.connection.write(self.stream.read(size))
                self.count += 1
                self.stream.seek(0)
        self.stream.write(buf)

#addrinfo = socket.getaddrinfo("225.1.1.1", None)[0]
#mcast_socket = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
#mcast_socket.connect(('225.1.1.1', 8123))
#connection = mcast_socket.makefile('wb')

client_socket = socket.socket()
client_socket.connect(('10.24.2.19', 8000))
connection = client_socket.makefile('wb')
try:

    output = SplitFrames(connection)
    with picamera.PiCamera(resolution='VGA', framerate=30) as camera:
        time.sleep(2)
        start = time.time()
        camera.start_recording(output, format='mjpeg')
        camera.wait_recording(30)
        camera.stop_recording()
        # Write the terminating 0-length to the connection to let the
        # server know we're done
        print("Writing packet")
        connection.write(struct.pack('<L', 0))

finally:
    connection.close()
    client_socket.close()
    finish = time.time()

print('Sent %d images in %d seconds at %.2ffps' % (
    output.count, finish-start, output.count / (finish-start)))
