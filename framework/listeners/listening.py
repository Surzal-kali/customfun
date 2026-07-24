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
    await writer.drain()
    writer.close()
    await writer.wait_closed()
    print("Connection closed")


async def listen(host, port, buffer_size):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Listening on {host}:{port} with buffer size {buffer_size}...")

    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        data = client.recv(buffer_size)
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
    parser.add_argument("--buffer-size", type=int, default=1024, help="Buffer size for incoming data")
    args = parser.parse_args()

    await listen(args.host, args.port, args.buffer_size)

if __name__ == "__main__":
    asyncio.run(main())