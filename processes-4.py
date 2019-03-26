proc = Popen(["docker", "login", "--password-stdin"], stdin=PIPE)
out, err = proc.communicate(my_password + "\n")