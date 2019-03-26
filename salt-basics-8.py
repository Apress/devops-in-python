# top.sls
base:
  '*':
    - core
    - monitoring
    - kubelet