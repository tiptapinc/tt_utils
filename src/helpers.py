import datetime
import uuid


def datetimeHandler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()


def uuid_me():
    return str(uuid.uuid4())


def now():
    return datetime.datetime.utcnow()


def now_isoformat():
	return datetime.datetime.utcnow().isoformat()