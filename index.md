---
layout: page
title: Community
subtitle: The computational biology community in Grenoble
---

# The computational biology community in Grenoble

<div class="community-layout">

<aside class="community-side">
  <img class="community-illustration" src="{{ site.baseurl }}/images/illustration.png" alt="The computational biology community in Grenoble">

  <div class="funding">
    <a href="https://persyval.univ-grenoble-alpes.fr/recherche/equipes-actions"><img src="{{ site.baseurl }}/images/logo-persyval_0.svg" alt="Persyval-Lab"></a>
    <p>The BIGRE! community is funded by a <a href="https://persyval.univ-grenoble-alpes.fr/recherche/equipes-actions">Persyval-Lab action team</a>.</p>
  </div>
</aside>

<div class="community-main">
  <p>A non-exhaustive list of labs and teams who do some form of computational biology in Grenoble and participate to the BIGRE! seminars:</p>

  <div class="lab-grid">
  {% assign labs = site.labs | sort: "path" %}
  {% for lab in labs %}
    <div class="lab-tile">
      {% if lab.image and lab.image != "" %}
        <img class="lab-image" src="{{ site.baseurl }}/images/labs/{{ lab.image }}" alt="{{ lab.name }}">
      {% else %}
        <span class="lab-image lab-image-placeholder">{{ lab.name }}</span>
      {% endif %}
      <div class="lab-body">
        <span class="lab-name">{{ lab.name }}</span>
        {% if lab.teams %}
        <div class="lab-teams"><strong>Teams:</strong>
          {% for team in lab.teams %}{% if team.url and team.url != "" %}<a href="{{ team.url }}">{{ team.name }}</a>{% else %}{{ team.name }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}
        </div>
        {% endif %}
        {% if lab.topics %}<div class="lab-topics">{{ lab.topics | join: " · " }}</div>{% endif %}
        <div class="lab-meta">
          {% if lab.permanent or lab.non_permanent %}
          {% assign total = lab.permanent | plus: lab.non_permanent %}
          <div class="lab-people"><strong>~{{ total }} people</strong></div>
          {% endif %}
          {% if lab.contacts %}<div><strong>Contact:</strong> {{ lab.contacts | join: ", " }}</div>{% endif %}
        </div>
      </div>
    </div>
  {% endfor %}
  </div>
</div>

</div>
