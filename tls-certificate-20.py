>>> private_bytes = service_private_key.private_bytes(
... encoding=serialization.Encoding.PEM,
... format=serialization.PrivateFormat.TraditionalOpenSSL,
... encryption_algorithm=serialization.NoEncrption())
>>> public_bytes = certificate.public_bytes(
... encoding=serialization.Encoding.PEM)
>>> with open("service.pem", "wb") as fout:
...     fout.write(private_bytes + public_bytes)