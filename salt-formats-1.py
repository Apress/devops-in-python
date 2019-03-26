{% if grains['os'] == 'CentOs' %}
python-devel:
{% elif grains['os'] == 'Debian' %}
python-dev:
{% else %}
{{ raise('Unrecognized operating system', grains['os']) }}
{% endif %}
  pkg:
    - installed