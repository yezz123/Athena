import binascii
import sys
from binascii import unhexlify

from cryptography.exceptions import InvalidKey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

password = sys.argv[1].encode()

try:
    salt = unhexlify(sys.argv[2].encode())
    key = unhexlify(sys.argv[3].encode())
except binascii.Error:
    print("Non-hexadecimal data on salt and/or key", file=sys.stderr)
    sys.exit(1)

backend = default_backend()

kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=backend)

try:
    kdf.verify(password, key)
    print("Valid")
except InvalidKey:
    print("Invalid")
