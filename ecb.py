#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Read flag
with open("flag", "r") as f:
    flag = f.read().strip()

# Read key
with open("enc_key", "r") as f:
    key_hex = f.read().strip()
key = bytes.fromhex(key_hex)

# Banner
welcome = """
************ MI6 Secure Encryption Service ************
                  [We're super secure]
       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
"""

# Padding to ensure the correct block length
def pad(message: str) -> bytes:
    padded = message + '1'
    while len(padded) % 16 != 0:
        padded += '0'
    return padded.encode()

# Encrypt using AES ECB
def encrypt():
    agent = input("Agent number: ")
    message = f"agent {agent} wants to see {flag}"
    padded = pad(message)

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return ciphertext.hex()

print(welcome)
print(encrypt())

