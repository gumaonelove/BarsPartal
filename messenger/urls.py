from django.urls import path

from .views import GetChatList, GetChat, SendMessage
urlpatterns = [
    path('get_chat_list/', GetChatList.as_view(), name='get_chat_list'),
    path('get_chat/', GetChat.as_view(), name='get_chat'),
    path('send_message/', SendMessage.as_view(), name='send_message')
]