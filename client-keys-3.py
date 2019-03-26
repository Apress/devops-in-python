>>> import os
>>> with open("key.priv", "w") as fp:
...    os.chmod(0o600, "key.priv")
...    k.write_private_key(fp)