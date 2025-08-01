import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key  : {key}")


# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
chipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    chipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {chipher_text}")


# DENCRYPT
chipher_text = input("Enter a message to dencrypt: ")
plain_text = ""

for letter in chipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {chipher_text}")
print(f"dencrypted message: {plain_text}")
