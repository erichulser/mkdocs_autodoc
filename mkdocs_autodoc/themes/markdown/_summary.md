{% for section, members in sections -%}
{% if section != 'Private Variable' -%}

### {{ section }}

<div class="well">
<ul class="list-unstyled">
{% for member, typ in members -%}
{% if member.kind == 'Enum' -%}
<li><a href="#{{ member.name }}">{{ member.name }}</a></li>
{% elif member.kind == 'Class' -%}
<li><a href="{{ member.url }}">{{ member.name }}</a></li> 
{% elif member.kind == 'Module' -%}
<li><a href="{{ member.url }}">{{ member.name }}</a></li>
{% elif 'Function' in member.kind or 'Method' in member.kind or 'Builtin' in member.kind -%}
<li>def <a href="#def-{{ member.name.lower() }}">{{ member.name }}</a>{{ member.args }}</li>
{% else -%}
<li>{{ member.name }} : {{ type }}</li>
{%- endif %}
{%- endfor %}</ul></div>
<ul>
{% for (url, name), section_members in member_map.items() %}
    {% if section_members.get(section) %}
    {% if url %}
    <li>{{ section_members[section] | length }} {{ section.lower() }}(s) inherited from <a href="{{ url }}">{{ name }}</a></li>
    {% else %}
    <li>{{ section_members[section] | length }} {{ section.lower() }}(s) inherited from <span class="text-danger">{{ name }}</li>
    {% endif %}
    {% endif %}
{% endfor %}
</ul>
{%- endif %}
{%- endfor %}