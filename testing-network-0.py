def get_files(gist_id):
    gist = requests.get(f"https://api.github.com/gists/{gist_id}").json()
    result = {}
    for name, details in gist["files"].items():
        result[name] = requests.get(details["raw_url"]).content
    return result