>>> builder = builder.add_extension(
... x509.BasicConstraints(ca=True, path_length=None),
... critical=True)