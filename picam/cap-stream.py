import io
import socket
import struct
import time
import picamera

port = 8123
addr = '225.1.1.1'
ttl = 2

print("Begin Capstream")

client_socket = socket.socket()
print("Begin Capstream")

client_socket.connect(('10.24.2.19', 1111))
print("Begin Capstream")

connection = client_socket.makefile('wb')
print("Begin Capstream")

print("Connection established")
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30
        time.sleep(2)
        start = time.time()
        count = 0
        stream = io.BytesIO()

        print("starting the stream")
        # Use the video-port for captures...
        for foo in camera.capture_continuous(stream, 'jpeg',
                                             use_video_port=True):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())

            print("wrote to network")
            count += 1
            if time.time() - start > 30:
                break
            stream.seek(0)
            stream.truncate()
    connection.write(struct.pack('<L', 0))
finally:
    print("Closing up shop")
    connection.close()
    client_socket.close()
    finish = time.time()
print('Sent %d images in %d seconds at %.2ffps' % (
    count, finish-start, count / (finish-start)))
