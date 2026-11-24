---
layout: page
title: Co-working
permalink: /coworking/
# Co-work sessions: one date per line, written dd/mm/yyyy.
# Past / next sessions are worked out automatically.
sessions:
  - "10/09/2026"
  - "15/10/2026"
  - "26/11/2026"
  - "17/12/2026"
  - "21/01/2027"
  - "18/02/2027"
  - "18/03/2027"
  - "27/05/2027"
  - "24/06/2027"
---

# Co-working

**We have a working group on molecular bioinformatics, with co-work sessions once a month, in the IMAG building.**

<div class="cowork-info">
  <div class="cowork-info-card">
    <i class="fa fa-map-marker" aria-hidden="true"></i>
    <span class="cowork-info-title">Where?</span>
    <span>Seminar Room 1, IMAG Building, Campus St Martin d’Hères.</span>
  </div>
  <div class="cowork-info-card">
    <i class="fa fa-clock-o" aria-hidden="true"></i>
    <span class="cowork-info-title">When?</span>
    <span>Once a month, Thursday mornings, from 8 to 12h.</span>
  </div>
  <div class="cowork-info-card">
    <i class="fa fa-laptop" aria-hidden="true"></i>
    <span class="cowork-info-title">How?</span>
    <span>Bring your laptop, your best computer bugs &amp; your good mood. We provide coffee, tea and cookies (bring your cup). Let’s work together!</span>
  </div>
  <div class="cowork-info-card">
    <i class="fa fa-lightbulb-o" aria-hidden="true"></i>
    <span class="cowork-info-title">What?</span>
    <span>A dedicated topic for each session, with a presentation by 1-2 member(s), time for discussion, and sometimes a hands-on practical session.</span>
  </div>
</div>

<div class="cowork-bonus">
  <i class="fa fa-cutlery" aria-hidden="true"></i>
  <span><strong>Bonus:</strong> followed by pizzas and the BIGRE seminar at 13h. <a href="{{ site.baseurl }}/seminars/">See the seminar program</a>.</span>
</div>

## Co-work schedule

{% assign month_names = "Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec" | split: "," %}
<div id="cowork-schedule" class="cowork-schedule">
{% for session in page.sessions %}
  {% assign d = session | strip | split: "/" %}
  {% assign m = d[1] | plus: 0 | minus: 1 %}
  <div class="cowork-session" data-date="{{ d[2] }}-{{ d[1] }}-{{ d[0] }}">
    <span class="talk-day">{{ d[0] }}</span>
    <span class="talk-month">{{ month_names[m] }}</span>
    <span class="talk-year">{{ d[2] }}</span>
  </div>
{% endfor %}
</div>

## Co-work members

<div class="member-grid">
{% for post in site.members %}
  {% include member-card.html %}
{% endfor %}
</div>

<script>
(function () {
  var today = new Date();
  today.setHours(0, 0, 0, 0);
  var nextFound = false;
  document.querySelectorAll('#cowork-schedule .cowork-session').forEach(function (s) {
    var d = new Date(s.dataset.date + 'T00:00:00');
    if (isNaN(d)) { return; }
    if (d < today) {
      s.classList.add('is-past');
    } else if (!nextFound) {
      s.classList.add('is-next');
      nextFound = true;
    }
  });
})();
</script>
