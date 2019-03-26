images = client.list(name="myusername/myrepo")
sofar = None
for image in images:
    maxtag = max(tag for tag in image.tags if tag.startswith("date-"))
    if sofar is None or maxtag > sofar:
        sofar = maxtag
        latest = image
latest.tag("myusername/myrepo", tag="latest")
client.push("myusername/myrepo", tag="latest")