import binascii
import sys
from binascii import unhexlify

import click
from cryptography.exceptions import InvalidKey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


@click.command()
@click.argument("key")
@click.argument("salt")
def crack_scrypt(key, salt):

    try:
        salt = unhexlify(sys.argv[1].encode())
        key = unhexlify(sys.argv[2].encode())
    except binascii.Error:
        print("Non-hexadecimal data on salt and/or key", file=sys.stderr)
        return False

    backend = default_backend()

    for number in range(10000):

        kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=backend)

        try:
            kdf.verify(str(number).encode(), key)
            print("Cracked! Password:", number)
            break
        except InvalidKey:
            pass


if __name__ == "__main__":
    crack_scrypt()
