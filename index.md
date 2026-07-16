---
layout: page
---

# BIGRE seminars 

Local and nationals speakers are invited to give talk on computational biology
covering subject from *computational biology*, *bioinformatics*,
*biostastics*, and *biophysics*.

Seminars are held in the IMAG auditorium ([150 Pl. du Torrent, 38400 Saint-Martin-d'Hères](https://maps.app.goo.gl/orJh7HWmtiXdX1mf6)).

To receive information about the seminar, subscribe to the [mailing
list](https://listes.univ-grenoble-alpes.fr/sympa/info/bigre-seminars).

## 2025-2026 seminars

{% for post in site.talks %}
    {% if post.series == "2025-2026" %}
        {% include archive-talk.html %}
    {% endif %}
{% endfor %}


## 2024-2025 seminars

{% for post in site.talks %}
    {% if post.series == "2024-2025" %}
        {% include archive-talk.html %}
    {% endif %}
{% endfor %}


