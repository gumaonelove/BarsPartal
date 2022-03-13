from json import loads

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from study.models import Event, Publications, Student, Parent, Teacher
from .forms import PublicationsForm, EventForm


class LoginView(View):
    '''Авторизация по логину и паролю'''
    def get(self, request):
        return render(request, 'auth.html')  # Страница входа

    def post(self, request, *args, **kwargs):
        action = loads(request.body)['action']
        username = loads(request.body)['username']
        password = loads(request.body)['password']

        if action == 'entry' or User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/study/profile/')
        else:
            new_user = User()
            new_user.username = username
            new_user.set_password(password)
            new_user.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/study/profile/')

        return render(request, 'main_page.html')  # Вход в систему


class EventsView(View):
    '''Мероприятия'''
    def get(self, request):
        if request.user.is_authenticated:
            student = Student.objects.filter(user=request.user)
            parent = Parent.objects.filter(user=request.user)
            teacher = Teacher.objects.filter(user=request.user)
            if student or parent or teacher:
                if student:
                    my_events = Student.objects.get(user=request.user).events.all()
                elif parent:
                    my_events = Parent.objects.get(user=request.user).events.all()
                else:
                    my_events = Teacher.objects.get(user=request.user).events.all()

                active_events = Event.objects.filter(active=True)
                form = EventForm(request.POST, request.FILES)
                context = {
                    'my_events': my_events,
                    'active_events': active_events,
                    'form': form
                }
                return render(request, 'events.html', context)
            else:
                return redirect('/study/personal_cub/')
        else:
            return redirect('/activity/auth/')

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=True)

            student = Student.objects.filter(user=request.user)
            parent = Parent.objects.filter(user=request.user)
            teacher = Teacher.objects.filter(user=request.user)

            if student:
                student.first().events.add(event)
                student.first().save()
            elif teacher:
                teacher.first().events.add(event)
                teacher.first().save()
            elif parent:
                parent.first().events.add(event)
                parent.first().save()

        return redirect('/activity/events/')


class PublicationsView(View):
    '''Публикации'''
    def get(self, request):
        if request.user.is_authenticated:
            student = Student.objects.filter(user=request.user)
            parent = Parent.objects.filter(user=request.user)
            teacher = Teacher.objects.filter(user=request.user)

            if student or parent or teacher:
                if student:
                    my_publications = Student.objects.get(user=request.user).publications.all()
                elif parent:
                    my_publications = Parent.objects.get(user=request.user).publications.all()
                else:
                    my_publications = Teacher.objects.get(user=request.user).publications.all()

                all_publications = Publications.objects.all()
                form = PublicationsForm(request.POST, request.FILES)

                context = {
                    'my_publications': my_publications,
                    'all_publications': all_publications,
                    'form': form
                }
                return render(request, 'publications.html', context)
            else:
                return redirect('/study/personal_cub/')
        else:
            return redirect('/activity/auth/')


    def post(self, request, *args, **kwargs):
        form = PublicationsForm(request.POST, request.FILES)
        if form.is_valid():
            new_pub = Publications.objects.create(
                author=request.user,
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                image=form.cleaned_data['image'],
            )
            new_pub.save()

            student = Student.objects.filter(user=request.user)
            parent = Parent.objects.filter(user=request.user)
            teacher = Teacher.objects.filter(user=request.user)

            if student:
                student.first().publications.add(new_pub)
                student.first().save()
            elif teacher:
                teacher.first().publications.add(new_pub)
                teacher.first().save()
            elif parent:
                parent.first().publications.add(new_pub)
                parent.first().save()

        return redirect('/activity/publications/')