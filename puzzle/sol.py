"""
Puzzle
Let's see how well you know your OFB.
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
from binascii import unhexlify
import secrets

def get_ekiv(first_ciphertext_block, first_block = b' '*16):
    n_first_ciphertext_block = int.from_bytes(first_ciphertext_block, byteorder='big')
    n_first_block = int.from_bytes(first_block, byteorder='big')
    return (n_first_block ^ n_first_ciphertext_block).to_bytes(16, 'big')

with open('flag.txt', 'rb') as file:
    data = file.read()
print(len(data))
data = pad(b'                ' + data, 16)
key = secrets.randbits(256).to_bytes(32, 'big')
enc1 = AES.new(key, AES.MODE_OFB)
iv1 = enc1.iv
ct1 = enc1.encrypt(data)
print(f"iv = {iv1}")
print(f"ct = {ct1}")

# user_input = input(("Give me a new IV in hex.\n"))
# if len(user_input) != 32: exit(0)
# iv2 = unhexlify(user_input.encode())
iv2 = get_ekiv(first_ciphertext_block=ct1[:16])
enc2 = AES.new(key, AES.MODE_OFB, iv=iv2)
ct2 = enc2.encrypt(data)
# print(f"Here's your new ciphertext: {ct2}")
cxorc = l2b(b2l(ct1) ^ b2l(ct2))
O = [iv2]
for i in range(0, len(cxorc), 16):
    o1 = l2b( b2l(O[-1]) ^ b2l(cxorc[i:i+16]) )
    O.append(o1)



# Now the magic happens
pt = b''
for i in range(0, len(ct1), 16):
    pt +=  l2b ( b2l(ct1[i:i+16]) ^ b2l(O[i//16]) )
print(pt)
with open('dec.txt', 'wb') as file: file.write(pt)