---
layout: page
---

# BIGRE seminars 

Local and nationals speakers are invited to give talk on computational biology
covering subject from *computational biology*, *bioinformatics*,
*biostastics*, and *biophysics*.

Seminars are typically held either in the IMAG auditorium or at the Pavillon
Taillefer in the TIMC laboratory.

To receive information about the seminar, subscribe to the [mailing
list](https://listes.univ-grenoble-alpes.fr/sympa/info/bigre-seminars).

## 2024-2025 seminars

{% for post in site.talks %}
    {% if post.series == "2024-2025" %}
        {% include archive-talk.html %}
    {% endif %}
{% endfor %}


## 2023-2024 seminars

{% for post in site.talks %}
    {% if post.series == "2023-2024" %}
        {% include archive-talk.html %}
    {% endif %}
{% endfor %}

