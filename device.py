import uuid
import hashlib

def get_device_id():
    # Menghasilkan device ID unik untuk 1 HP
    raw = str(uuid.getnode()).encode()
    return hashlib.md5(raw).hexdigest()
