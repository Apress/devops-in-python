Extract archive:
  archive.extracted:
    - name: /src/some-files
    - source: /src/some-files.tgz
    - archive_format: tar
Copy archive:
  file.managed:
    - name: /src/some-files.tgz
    - source: salt://some-files.tgz
  - require_in:
    - archive: Extract archive.