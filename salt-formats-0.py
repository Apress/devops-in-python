{% if grains['os'] == 'CentOs' %}
python-devel:
{% elif grains['os'] == 'Debian' %}
python-dev:
{% endif %}
  pkg:
    - installed