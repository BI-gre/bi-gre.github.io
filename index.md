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

You can add our shared google calendar following this [link](https://calendar.google.com/calendar/u/0?cid=MjhjMmExMjc5YmU2MGM5MTY2YmMxYjcyMzc3ZmFhNGZiNGQ2NzM0ZTRjNGVkY2NiOGMwYjFiZDg5YWVhN2ZkY0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t).

## 2026-2027 seminars

{% for post in site.talks %}
    {% if post.series == "2026-2027" %}
        {% include archive-talk.html %}
    {% endif %}
{% endfor %}

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


