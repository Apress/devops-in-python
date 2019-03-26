def analyze_debian_paths(relative_to='/'):
    sources_dir = os.path.join(relative_to, 'etc/apt/sources.list.d')
    for fname in os.listdir(sources_dir):
        with open(os.path.join(sources_dir, fname)) as fpin:
            yield from _analyze_debian_paths_from_file(fpin)