def add_to_docker(username):
    subprocess.check_call(["usermod", "-G", "docker", username])