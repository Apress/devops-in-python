---
- hosts: all
  tasks:
    - name: hello printer
      shell: echo "hello world" >> /etc/hello