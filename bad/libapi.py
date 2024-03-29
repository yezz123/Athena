import hashlib
import random
from pathlib import Path

import libuser


def keygen(username, password=None):

    if password and not libuser.login(username, password):
        return None

    key = hashlib.sha256(str(random.getrandbits(2048)).encode()).hexdigest()

    for f in Path("/tmp/").glob("Athena.apikey." + username + ".*"):
        print("removing", f)
        f.unlink()

    keyfile = f"/tmp/Athena.apikey.{username}.{key}"

    Path(keyfile).touch()

    return key


def authenticate(request):
    if "X-APIKEY" not in request.headers:
        return None

    key = request.headers["X-APIKEY"]

    for f in Path("/tmp/").glob("Athena.apikey.*." + key):
        return f.name.split(".")[2]

    return None
