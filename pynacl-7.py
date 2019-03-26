>>> from nacl.public import PrivateKey, PublicKey, Box
>>> with open("source.pubkey", "rb") as fpin:
...     source_public_key = PublicKey(fpin.read())
>>> with open("target.private_key", "rb") as fpin:
...     target = PrivateKey(fpin.read())
>>> dec_box = Box(target, source_public_key)
>>> dec_box.decrypt(result)
b'x marks the spot'