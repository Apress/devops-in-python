with open("/etc/fstab") as fpin:
    for line in fpin:
        line = line.rstrip('\n')
        line = line.split('#', 1)[0]
        if not line:
            continue
        device, path, fstype, options, freq, passno = line.split()
        print(f"Mounting {device} on {path}")