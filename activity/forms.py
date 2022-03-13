from django.forms import ModelForm
from study.models import Achievements, Publications, Event


class AchievementsForm(ModelForm):
    class Meta:
        model = Achievements
        fields = '__all__'


class PublicationsForm(ModelForm):
    class Meta:
        model = Publications
        fields = ['title', 'text', 'image']


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'