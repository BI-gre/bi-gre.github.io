---
layout: page
title: Seminars
permalink: /seminars/
---

# BIGRE seminars 

Local and nationals speakers are invited to give talk on computational biology
covering subject from *computational biology*, *bioinformatics*,
*biostastics*, and *biophysics*.

Seminars are held in the IMAG auditorium ([150 Pl. du Torrent, 38400 Saint-Martin-d'Hères](https://maps.app.goo.gl/orJh7HWmtiXdX1mf6)).

To receive information about the seminar, subscribe to the [mailing
list](https://listes.univ-grenoble-alpes.fr/sympa/info/bigre-seminars).

You can add our shared google calendar following this [link](https://calendar.google.com/calendar/u/0?cid=MjhjMmExMjc5YmU2MGM5MTY2YmMxYjcyMzc3ZmFhNGZiNGQ2NzM0ZTRjNGVkY2NiOGMwYjFiZDg5YWVhN2ZkY0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t).

{% comment %}
  Nothing to edit here: upcoming / past seminars and the "next seminar"
  are worked out automatically in the browser from each talk's date.
{% endcomment %}

<div class="seminars">

<div id="next-seminar" class="next-seminar" hidden>
  <h2>Next seminar</h2>
</div>

<div id="upcoming-section" hidden>
  <h2>Upcoming seminars</h2>
  <div id="upcoming-list" class="talk-list"></div>
</div>

<details id="past-seminars" class="past-seminars" open>
  <summary>Past seminars</summary>
  {% assign seasons = site.talks | group_by: "series" | sort: "name" | reverse %}
  {% for season in seasons %}
  <div class="talk-season">
    <h3>{{ season.name }}</h3>
    <div class="talk-list">
    {% assign season_talks = season.items | sort: "path" | reverse %}
    {% for post in season_talks %}
      {% include talk-card.html %}
    {% endfor %}
    </div>
  </div>
  {% endfor %}
</details>

</div>

<script>
(function () {
  var today = new Date();
  today.setHours(0, 0, 0, 0);
  var upcoming = [];

  document.querySelectorAll('#past-seminars .talk-card').forEach(function (card) {
    var d = new Date(card.dataset.date + 'T00:00:00');
    if (!isNaN(d) && d >= today) { upcoming.push({ date: d, card: card }); }
  });
  upcoming.sort(function (a, b) { return a.date - b.date; });

  if (upcoming.length) {
    var next = upcoming.shift().card;
    next.classList.add('is-next');
    var box = document.getElementById('next-seminar');
    box.appendChild(next);
    box.hidden = false;
  }
  if (upcoming.length) {
    var list = document.getElementById('upcoming-list');
    upcoming.forEach(function (u) { list.appendChild(u.card); });
    document.getElementById('upcoming-section').hidden = false;
  }

  // Hide seasons left empty, then fold the past seminars away
  document.querySelectorAll('.talk-season').forEach(function (s) {
    if (!s.querySelector('.talk-card')) { s.hidden = true; }
  });
  document.getElementById('past-seminars').open = false;
})();
</script>

