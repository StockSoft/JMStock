<!DOCTYPE html>
<html lang="en">
    <head>
        <title> {% block title %} JMStock {% endblock %}</title>
        <meta charset='utf-8' />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="/static/css/bootstrap.min.css" rel="stylesheet">
        {% block header %}{% endblock %}
    </head>

    <body>
        {% block content %}
        {% endblock %}

        <!-- Bootstrap core JavaScript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="/static/js/jquery.min.js"></script>
        <script src="/static/js/bootstrap.min.js"></script>
        {% block js%}{% endblock %}
    </body>
</html>

