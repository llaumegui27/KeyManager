import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

def password_declaration():
    """
    Ask user to enter and confirm a password
    """
    while True:
        password = input("Enter your password: ")
        password_check = input("Confirm your password: ")
        if password == password_check:
            return password
        print("Passwords do not match. Try again.\n")


def derive_key(password: str, salt: bytes) -> bytes:
    """
    Derive an AES-256 key from a password using PBKDF2-HMAC-SHA256.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


def encrypt_file(input_path: str, output_path: str, password: str):
    """
    File encryption with AES-256-GCM.
    Output file format : [salt (16 bytes)] [nonce (12 bytes)] [ciphertext + tag]
    """
    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    with open(input_path, "rb") as f:
        plaintext = f.read()

    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    with open(output_path, "wb") as f:
        f.write(salt + nonce + ciphertext)

    print("✔ File encrypted:", output_path)


def decrypt_file(input_path: str, output_path: str, password: str):
    """
    Decrypt the AES-GCM file built by encrypt_file.
    """
    with open(input_path, "rb") as f:
        data = f.read()

    salt = data[:16]
    nonce = data[16:28]
    ciphertext = data[28:]

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    with open(output_path, "wb") as f:
        f.write(plaintext)

    print("✔ File decrypted:", output_path)

