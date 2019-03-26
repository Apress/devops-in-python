def error_lines(container_name, executor):
    logs, _ignored = executor.docker.logs(container_name).batch()
    for line in logs.splitlines():
        if 'error' in line:
            yield line.strip()