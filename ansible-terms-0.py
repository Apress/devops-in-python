- hosts: databases
  remote_user: ubuntu
  become: True

  tasks:
  - name: ensure that postgresql is started
    service:
      name: postgresql
      state: started