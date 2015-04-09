{% for member in members -%}
{% if member.kind not in ('Module', 'Class', 'Member', 'Variable', 'Signal', 'Slot', 'Property') -%}
<div class="panel panel-default"><div class="panel-body">
{% if 'Static' in member.kind or 'Class' in member.kind or 'Protected' in member.privacy or 'Private' in member.privacy -%}
<div class="page-header">
    <h3>
        def <a name="def-{{ member.name.lower() }}" class="text-success">{{ member.name.replace('_', '\_') }}{{ member.args }}</a>
        <span class="pull-right"><small><strong>[{{ member.privacy.lower() }} {{ member.kind.lower() }}]</strong></small></span>
    </h3>
</div>
{% else -%}
<div class="page-header">
    <h3>
        def <a name="def-{{ member.name.lower() }}" class="text-success">{{ member.name.replace('_', '\_') }}{{ member.args }}</a>
    </h3>
</div>
{%- endif %}
{% if member.reimpliments -%}
_Reimpliments: {{ member.reimpliments }}_
{%- endif %}
{% if member.reimplimented -%}
_Reimplimented: {{ member.reimplimented }}_
{%- endif %}
{% if member.raw_docs -%}
{{ member.wikitext_docs }}
{%- endif %}
</div></div>
{%- endif %}
{%- endfor %}