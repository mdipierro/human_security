# Security for Humans

It is a thin layer on top of the cryptography module. Exposes an easy to use interface to EAS and RSA.

## Symmetric encryption

The same key is used for encryption and decryption

```
from human_security import HumanAES
h = HumanAES()
h.generate()
saved_key = h.key

h = HumanAES()
h.key = saved_key
message = 'hello world'
encrypted = h.encrypt(message)
decrypted = h.decrypt(encrypted)
assert decrypted == message
```


## Asymmetric encryption

A public key `public_pem` is used to encrypt and the corresponding `private_pem` is used for decryption

```
from human_security import HumanRSA

h = HumanRSA()
h.generate()
# save keys
public_pem = h.public_pem()
private_pem = h.private_pem()
# reload saved keys

h = HumanRSA()
h.load_public_pem(public_pem)
encrypted = h.encrypt(message)

h = HumanRSA()
h.load_private_pem(private_pem)
decrypted = h.decrypt(encrypted)
assert decrypted == message
```

## Signatures

The `public_pem` is used to sign and the `private_pem` is used to verify the signature

```
from human_security import HumanRSA
h = HumanRSA()
h.load_private_pem(private_pem)
signature = h.sign(message)

h = HumanRSA()
h.load_public_pem(public_pem)
assert h.verify(message, signature)
```

