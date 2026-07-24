import random

def xor_cipher(data, key):
    return bytes([b ^ key for b in data])

def encode_payload(input_file, output_file):
    key = random.randint(1, 255)
    with open(input_file, 'rb') as f:
        original = f.read()
    
    encoded = xor_cipher(original, key)
    
    # Write the key to the top of the file so the loader knows how to decrypt it
    with open(output_file, 'wb') as f:
        f.write(bytes([key]) + encoded)
    
    print(f"[*] Payload encoded with key {hex(key)} -> {output_file}")
