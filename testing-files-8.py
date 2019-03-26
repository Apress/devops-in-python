def _analyze_debian_paths_from_file(fpin):
    for line in fpin:
        line = line.strip()
        if not line:
            continue
        line = line.split('#', 1)[0]
        parts = line.split()
        if parts[0] != 'deb':
            continue
        if parts[1][0] == '[':
            del parts[1]
        parsed = hyperlink.URL.from_text(parts[1].decode('ascii'))
        yield parsed.host