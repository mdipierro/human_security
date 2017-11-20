# Security for Humans


## Symmetric encryption

The same key is used for encryption and decryption

```
from human_security import HumanAES
message = 'hello world'
h = HumanAES()
h.generate()
print h.key 
encrypted = h.encrypt(message)
decrypted = h.decrypt(encrypted)
assert decrypted == message
```


## Asymmetric encryption

A public key is used to encrypt and the corresponding private_key is used for decryption

```
from human_security import HumanRSA

h = HumanRSA()
h.generate()
# save keys
public_pem = h.public_pem()
private_pem = h.private_pem()
# reload saved keys
h.load_public_pem(public_pem)
h.load_private_pem(private_pem)
encrypted = h.encrypt(message)
decrypted = h.decrypt(encrypted)
assert decrypted == message
```

## Signatures

The public_key is used to sign and the private_key is used to verify the signature

```
from human_security import HumanRSA
h = HumanRSA()
h.generate()
signature = h.sign(message)
assert h.verify(message, signature)
```

