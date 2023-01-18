import pyaudio
from vidstream import AudioReceiver

import socket
import threading

port = 5000
host = ""

reciever = AudioReceiver(host, port, channels=2)
recieve_thread = threading.Thread(target=reciever.start_server)

recieve_thread.start()
