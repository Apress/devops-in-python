sha = subprocess.check_output(
          ["git", "rev-parse", "HEAD"],
          cwd="src/some-project").decode("ascii").strip()