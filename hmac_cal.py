import hmac
import hashlib
import binascii

# The secret key you found in the APK
# If it's hex format:
key = binascii.unhexlify('8c34bac50d9b096d41cafb53683b315690acf65a11b5f63250c61f7718fa1d1d')

# If it's a string (e.g., base64):
# key = b'your_hmac_key_string'

with open("magisk_ssl.zip", 'rb') as f:
    data = f.read()

# The algorithm is often MD5 or SHA256
h = hmac.new(key, data, hashlib.md5)  # or hashlib.sha256
print(h.hexdigest())