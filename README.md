# Security for Humans


## Symmetric encryption
```
from human_security import HumanAES, HumanRSA

message = 'hello world'
h = HumanAES()
h.generate()
print h.key
assert h.decrypt(h.encrypt(message)) == message
```


## Asymmetric encryption
```
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
```
h = HumanRSA()
h.generate()
signature = h.sign(message)
assert h.verify(message, signature)
```

