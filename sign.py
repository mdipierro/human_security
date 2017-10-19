#
# Author: Massimo Di Pierro
# License: MIT
#

import rsa
import json
import base64

def make_keys():
    (pubkey, privkey) = rsa.newkeys(512)
    return {'public_key': pubkey._save_pkcs1_pem(),
            'private_key':privkey._save_pkcs1_pem()}

def sign(data, private_key):
    privkey = rsa.PrivateKey.load_pkcs1(private_key)
    signature = base64.b64encode(rsa.sign(str(data), privkey, 'SHA-1'))    
    return signature

def verify(data, signature, public_key):
    pubkey = rsa.PublicKey.load_pkcs1(public_key)
    signature = base64.b64decode(signature)
    return rsa.verify(data, signature, pubkey)

def test():
    keys = make_keys()
    public_key = keys['public_key']
    private_key = keys['private_key']
    data = '1234567890'
    signature = sign(data, private_key)
    assert verify(data, signature, public_key)

if __name__ == '__main__':
    test()
