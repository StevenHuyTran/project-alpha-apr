# {% extends 'base.html' %}
# {% block content %}
#     <main>
#       <div>
#         <h1>Create Receipt</h1>
#         <form method="post">
#           {% csrf_token %} {{ form.as_p }}
#           <button>Create</button>
#         </form>
#       </div>
#     </main>
# {% endblock content %}
#   </body>
# </html>