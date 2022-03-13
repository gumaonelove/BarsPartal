from json import loads

from django.shortcuts import render, redirect
from django.views import View


from study.models import Student, Parent, Teacher, Subject
from activity.forms import AchievementsForm


class ProfileView(View):
    '''main page view'''
    def get(self, request):
        if request.user.is_authenticated:

            student = Student.objects.filter(user=request.user)
            parent = Parent.objects.filter(user=request.user)
            teacher = Teacher.objects.filter(user=request.user)

            if student or parent or teacher:
                form = AchievementsForm(request.POST, request.FILES)
                achievements = []
                context = {}

                if student:
                    achievements = student.first().achievements.all()
                    context['human'] = student.first()
                    context['position'] = 'student'
                elif teacher:
                    achievements = teacher.first().achievements.all()
                    context['human'] = teacher.first()
                    context['position'] = 'teacher'
                elif parent:
                    context['human'] = parent.first()
                    context['position'] = 'parent'

                    for child in parent.first().child.all():
                        achievements += child.achievements.all()

                context['form'] = form
                context['achievements'] = achievements

                return render(request, 'profile.html', context)
            else:
                return redirect('/study/personal_cub/')
        else:
            return redirect('/activity/auth/')

    def post(self, request, *args, **kwargs):
        form = AchievementsForm(request.POST, request.FILES)
        if form.is_valid():
            new_achievement = form.save(commit=True)

            student = Student.objects.filter(user=request.user)
            parent = Parent.objects.filter(user=request.user)
            teacher = Teacher.objects.filter(user=request.user)

            if student:
                student.first().achievements.add(new_achievement)
                student.first().save()
            if parent:
                parent.first().achievements.add(new_achievement)
                parent.first().save()
            if teacher:
                teacher.first().achievements.add(new_achievement)
                teacher.first().save()

        return redirect('/study/profile/')


class TutorsView(View):
    '''Репетиторы'''
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            student = Student.objects.filter(user=request.user)
            parent = Parent.objects.filter(user=request.user)
            teacher = Teacher.objects.filter(user=request.user)

            if student or parent or teacher:
                subject = kwargs.get('subject')
                subjects = Subject.objects.all()

                if subject == 'all':
                    tutors = Teacher.objects.filter(is_tutor=True)
                    subject = False
                else:
                    tutors = Teacher.objects.filter(subject__name=subject)

                context = {
                    'tutors': tutors,
                    'subjects': subjects,
                    'subject': subject
                }
                return render(request, 'tutors.html', context)
            else:
                return redirect('/study/personal_cub/')
        else:
            return redirect('/activity/auth/')


class PersonalCubView(View):
    '''Персональный кабинет'''

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            student = Student.objects.filter(user=request.user)
            parent = Parent.objects.filter(user=request.user)
            teacher = Teacher.objects.filter(user=request.user)
            context = {}
            if student:
                context['human'] = student.first()
                context['position'] = 'student'
            elif teacher:
                context['human'] = teacher.first()
                context['position'] = 'teacher'
            elif parent:
                context['human'] = parent.first()
                context['position'] = 'parent'
            subjects = Subject.objects.all()
            context['subjects'] = subjects

            return render(request, 'personal_cub.html', context)
        else:
            return redirect('/activity/auth/')


    def post(self, request):
        surname = loads(request.body)['surname']
        name = loads(request.body)['name']
        lastname = loads(request.body)['lastName']
        image = loads(request.body)['image']
        position = loads(request.body)['position']
        date = loads(request.body)['date']

        if position == '1':
            new_teacher = Teacher.objects.create(
                user=request.user,
                surname=surname,
                name=name,
                lastname=lastname,
                date_of_birth=date,
                subject=Subject.objects.get(name=loads(request.body)['subject']),
                text=loads(request.body)['text'],
                is_tutor=True if loads(request.body)['subject'] == 'Да' else False
            )
            new_teacher.save()
        elif position == '2':
            new_student = Student.objects.create(
                user=request.user,
                surname=surname,
                name=name,
                lastname=lastname,
                date_of_birth=date,
                school_class=loads(request.body)['school_class']
            )
            new_student.save()
        else:
            child_login = loads(request.body)['child_login']
            student = Student.objects.get(username=child_login)

            parent = Parent.objects.create(user=request.user,
                surname=surname,
                name=name,
                lastname=lastname,
                date_of_birth=date,
            )
            parent.save()
            parent.child.add(student)
            parent.save()

        return redirect('/study/profile/')