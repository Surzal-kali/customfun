import re
import sys
import os
import asyncio
import socket
from asyncio import StreamReader, StreamWriter
import argparse

async def handle(reader: StreamReader, writer: StreamWriter):
    data = await reader.read(100)
    print(f"Received: {data.decode()}")
    writer.write(data)
    await writer.drain
    writer.close()
    await writer.wait_closed()
    print("Connection closed")


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
        return addr

async def background_task():
    while True:
        await asyncio.sleep(1)
        print("Background task running")

async def main():
    parser = argparse.ArgumentParser(description="Simple TCP server.")
    parser.add_argument("port", type=int, help="Port to listen on")
    parser.add_argument("--host", default="0.0.0.0", help="Host to connect to")
    args = parser.parse_args()

    await listen(args.port)

if __name__ == "__main__":
    asyncio.run(main())