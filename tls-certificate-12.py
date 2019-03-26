>>> from cryptography.hazmat.primitives import serialization
>>> private_bytes = private_key.private_bytes(
... encoding=serialization.Encoding.PEM,
... format=serialization.PrivateFormat.TraditionalOpenSSL,
... encryption_algorithm=serialization.NoEncrption())
>>> public_bytes = certificate.public_bytes(
... encoding=serialization.Encoding.PEM)
>>> with open("ca.pem", "wb") as fout:
...     fout.write(private_bytes + public_bytes)
>>> with open("ca.crt", "wb") as fout:
...     fout.write(public_bytes)