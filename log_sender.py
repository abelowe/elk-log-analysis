import socket
import json
import random
import time

HOST = 'localhost'
PORT = 5001  

users = ['admin', 'root', 'user1', 'guest', 'john']
statuses = ['success', 'fail']

while True:
    log = {
        "message": "login attempt",
        "user": random.choice(users),
        "status": random.choice(statuses),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            s.sendall((json.dumps(log) + '\n').encode('utf-8'))
        except Exception as e:
            print("Error sending log:", e)

    time.sleep(2)  
