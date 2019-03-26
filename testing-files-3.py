def javascript_to_python_3(dirname):
    for path in pathlib.Path(dirname).iterdir():
        if path.suffix == '.js':
            path.rename(path.parent.joinpath(path.stem + '.py'))