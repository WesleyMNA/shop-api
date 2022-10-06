from hashlib import sha256


def encrypt_password(raw_password: str):
    return sha256(raw_password.encode()).hexdigest()


def password_is_valid(passed_password: str, db_password: str):
    hashed_password = encrypt_password(passed_password)
    return hashed_password == db_password
