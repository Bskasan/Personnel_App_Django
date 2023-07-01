from django.urls import path, include
from .views import RegisterView, ProfileUpdateView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
    path('profile/<int:pk>/', ProfileUpdateView.as_view()),
]

# An API endpoint is a point at which an API -- the code that allows two software programs to communicate with each other -- connects with the software program. APIs work by sending requests for information from a web application or web server and receiving a response.

# Systems that communicate through APIs are integrated systems. One side sends the information to the API and is called the server. The other side, the client, makes the requests and manipulates the API. The server side that provides the requested information, or resources, is the API endpoint.