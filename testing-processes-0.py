def error_lines(container_name):
    logs = subprocess.check_output(["docker", "logs", container_name])
    for line in logs:
        if 'error' in line:
            return line