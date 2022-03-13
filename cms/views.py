from django.shortcuts import render
from django.views import View

from cms.models import Developer


class MainPageView(View):
    '''main page view'''

    def get(self, request):
        developers = Developer.objects.all().order_by('-id')

        context = {
            'developers': developers
        }
        return render(request, 'main_page.html', context)
