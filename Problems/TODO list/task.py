template = """
<html>
  <ul>
  {% for task in todos %}
    <li> {{ task }} </li>
  {% endfor %}
  </ul>
</html>
"""
