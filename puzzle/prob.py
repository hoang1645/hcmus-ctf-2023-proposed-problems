"""
Puzzle
Let's see how well you know your OFB.
"""


"""
Challenge used on a netcat-able server
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from binascii import unhexlify
import secrets

with open('flag.txt', 'rb') as file:
    data = file.read()

data = pad(b'                ' + data, 16)
key = secrets.randbits(256).to_bytes(32, 'big')
enc1 = AES.new(key, AES.MODE_OFB)
iv1 = enc1.iv
ct1 = enc1.encrypt(data)
print(f"iv = {iv1}")
print(f"ct = {ct1}")


user_input = input(("Give me a new IV in hex.\n"))
assert len(user_input) == 32
iv2 = unhexlify(user_input.encode())
enc2 = AES.new(key, AES.MODE_OFB, iv=iv2)
ct2 = enc2.encrypt(data)
print(f"Here's your new ciphertext: {ct2}")
