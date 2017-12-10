# Created by Massimo Di Pierro
# Entirely based on documentation from https://cryptography.io/
# Hosted at https://github.com/mdipierro/human_security
# License BSD

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet

class HumanAES(object):
    def __init__(self, key=None):
        self.key = key        
    def generate(self):
        self.key = Fernet.generate_key()
    def encrypt(self, value):
        fernet = Fernet(self.key)
        return fernet.encrypt(value)
    def decrypt(self, value):
        fernet = Fernet(self.key)
        return fernet.decrypt(value)

class HumanRSA(object):
    def __init__(self):
        self.pad = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
            )
    def generate(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend())
        self.public_key = self.private_key.public_key()
    def private_pem(self):
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption())
    def public_pem(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo)
    def load_private_pem(self, pem):
        self.private_key = load_pem_private_key(pem, password=None, backend=default_backend())
    def load_public_pem(self, pem):
        self.public_key = load_pem_public_key(pem, backend=default_backend())
    def encrypt(self, data):
        return self.public_key.encrypt(data, self.pad)
    def decrypt(self, data):
        return self.private_key.decrypt(data, self.pad)
    def sign(self, data):
        return self.private_key.sign(
            data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())
    def verify(self, data, signature):
        try:
            self.public_key.verify(
                signature,
                data,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256())
            return True
        except InvalidSignature:
            return False
            
def example():
    message = 'hello world'
    h = HumanAES()
    h.generate()
    assert h.decrypt(h.encrypt(message)) == message

    h = HumanRSA()
    h.generate()
    print h.public_pem()
    print h.private_pem()

    encrypted = h.encrypt(message)
    decrypted = h.decrypt(encrypted)
    assert decrypted == message
    signature = h.sign(message)
    assert h.verify(message, signature)

if __name__ == '__main__':
    example()
