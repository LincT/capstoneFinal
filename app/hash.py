
import uuid
import hashlib


class HashConverter:
    @staticmethod
    def convert(string):
        hashString = ""
        if string != "":
            hashString = hashlib.sha1(string)
        return hashString


# https://www.pythoncentral.io/hashing-strings-with-python/
class HashTest:
    @staticmethod
    def hash_password(password):
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    @staticmethod
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
