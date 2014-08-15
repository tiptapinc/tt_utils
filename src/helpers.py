import datetime
import hashlib
import random
import uuid


def datetimeHandler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()


def uuid_me():
    return str(uuid.uuid4())


def random_sha():
    salt_seed = str(random.getrandbits(256))
    salted = hashlib.sha256(salt_seed).hexdigest()
    return salted


def now():
    return datetime.datetime.utcnow()


def now_isoformat():
    return datetime.datetime.utcnow().isoformat()
