>>> from cryptography.x509.oid import NameOID
>>> builder = builder.subject_name(x509.Name([
... x509.NameAttribute(NameOID.COMMON_NAME, 'Simple Test CA'),
... ]))
>>> builder = builder.issuer_name(x509.Name([
... x509.NameAttribute(NameOID.COMMON_NAME, 'Simple Test CA'),
... ]))