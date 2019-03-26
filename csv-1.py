def write_attempts(attempts, fname):
    with open(fname, 'w') as fpout:
        writer = csv.writer(fpout)
        writer.writerow(['Username', 'Timestamp', 'Success'])
        for attempt in attempts:
            writer.writerow([
                attempt.username,
                attempt.time_stamp,
                str(attempt.success),
            ])