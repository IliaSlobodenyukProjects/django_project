import hashlib

hash_object_md5 = hashlib.md5(b'9999')
print(hash_object_md5.hexdigest())

hash_object_sha256 = hashlib.sha256(b'user')
print(hash_object_sha256.hexdigest())
