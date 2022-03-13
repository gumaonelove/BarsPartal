from json import loads

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views import View

from .models import Chat, Message_chat


class GetChatList(View):
    '''Отправляю чаты пользователя'''
    def get(self, request):
        if request.body:
            username = loads(request.body)['username']
            password = loads(request.body)['password']
            user = authenticate(username=username, password=password)

            if user:
                context = {}

                for chat in Chat.objects.all():
                    if user in chat.members.all():
                        context[chat.id] = {'chat_name': chat.chat_name}
                        context[chat.id]['last_message'] = chat.last_message.message
                        context[chat.id]['last_type'] = chat.last_message.type

                context['error'] = False
                return JsonResponse(context)
            else:
                return JsonResponse({'error': True})
        else:
            return JsonResponse({'error': True})


class GetChat(View):
    ''''''
    def get(self, request):
        username = loads(request.body)['username']
        password = loads(request.body)['password']

        user = authenticate(username=username, password=password)

        if user:
            chat_id = loads(request.body)['chat_id']
            messages = {}
            members = {}

            chat = Chat.objects.filter(id=chat_id)
            if chat:
                chat = chat.first()
                for message in chat.messages.all():
                    messages[message.id] = {'chat_id': message.chat.id}
                    messages[message.id]['author_id'] = message.author.id
                    messages[message.id]['message_type'] = message.type
                    messages[message.id]['message'] = message.message
                    messages[message.id]['pub_date'] = message.pub_date
                    messages[message.id]['is_readed'] = message.is_readed

                    message.is_readed = True
                    message.save()

                for member in chat.members.all():
                    members[member.id] = member.username

                context = {
                    'messages': messages,
                    'members': members,
                    'error': False
                }

                return JsonResponse(context)
            else:
                return JsonResponse({
                    'error': True,
                    'error_name': 'incorrect chat_id'
                })
        else:
            return JsonResponse({
                'error': True,
                'error_name': 'incorrect login or password'
            })


class SendMessage(View):
    '''send mes'''

    def post(self, request):
        username = loads(request.body)['username']
        password = loads(request.body)['password']

        user = authenticate(username=username, password=password)

        if user:
            chat_id = loads(request.body)['chat_id']
            file = loads(request.body)['file']
            type_file = loads(request.body)['type_file']

            message = Message_chat.objects.create(
                chat=Chat.objects.get(id=chat_id),
                author=user,
                message=file,
                type=type_file,
                is_readed=False
            )
            message.save()

            chat = Chat.objects.get(id=chat_id)
            chat.messages.add(message)
            chat.last_message = message
            chat.save()

            return JsonResponse({'error': False})

        else:
            return JsonResponse({'error': True})