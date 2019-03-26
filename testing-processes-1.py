def error_lines(container_name, runner=subprocess.check_output):
    logs = runner(["docker", "logs", container_name])
    for line in logs:
        if 'error' in line:
            yield line.strip()