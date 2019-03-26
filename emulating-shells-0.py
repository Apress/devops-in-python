>>> channel = client.invoke_shell()
>>> input = channel.makefile("wb")
>>> output = channel.makefile("rb")