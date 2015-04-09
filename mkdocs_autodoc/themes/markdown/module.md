<h1>{{ title.split('.')[-1] }} <small>[module documentation]</small></h1>

{% if brief %}
{{ brief }} [More...](#details)
{% elif page.raw_docs %}
{{ page.wikitext_docs }}
{% endif %}

{% include '_summary.md' %}

{% if brief %}
Details
------------------
{{ page.wikitext_docs }}
{% endif %}

Functions
------------------
{% include '_details.md' %}

