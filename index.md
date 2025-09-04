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

Find speakers slides [here](https://cloud.univ-grenoble-alpes.fr/apps/files/files/1037979240?dir=/BIGRE/S%C3%A9minaires/Saison%202025-2026/Diapos_speakers).


## 2024-2025 seminars

{% for post in site.talks %}
    {% if post.series == "2024-2025" %}
        {% include archive-talk.html %}
    {% endif %}
{% endfor %}


Find speakers slides [here](https://cloud.univ-grenoble-alpes.fr/apps/files/files/1011834450?dir=/BIGRE/S%C3%A9minaires/Saison%202024-2025/Diapos_speakers).

## 2023-2024 seminars

{% for post in site.talks %}
    {% if post.series == "2023-2024" %}
        {% include archive-talk.html %}
    {% endif %}
{% endfor %}

