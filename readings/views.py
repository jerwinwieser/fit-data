from django.shortcuts import render
from readings.models import Title


def index(request):
    content = {
            'titles': Title.objects.all()
            }
    return render(request, 'readings/home.html', content)
