from django.urls import path  
from .views import send_message, show_messages

app_name = "messaging"

urlpatterns = [ 
    path("send/", send_message, name="send_message"),
    path("inbox/", show_messages, name="show_messages"),
]
