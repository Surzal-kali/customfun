import re
import sys
import os
import asyncio
import socket

async def listen(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen()
    print(f"Listening on port {port}...")

    while True:
        client, addr = await server.accept()
        print(f"Connection from {addr}")
        data = client.recv(1024) #TODO: add buffer size as a variable
        print(f"Received: {data.decode()}")
        client.close()

if __name__ == "__main__":
    port = 8080
    asyncio.run(listen(port))