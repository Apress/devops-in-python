def analyze_debian_paths():
    for fname in os.listdir('/etc/apt/sources.list.d'):
        with open(os.path.join('/etc/apt/sources.list.d', fname)) as fpin:
            yield from _analyze_debian_paths_from_file(fpin)