from django.shortcuts import render
from apps.main.models import Carousel, About, Expertise

def index(request):
    carousels = Carousel.objects.filter(active=True)
    carousel_first = carousels[0]
    carousels = carousels[1:]

    # about
    about = About.objects.filter(active=True)[:1]
    about[0].title = f'{about[0].text[:17]}...'

    # expertise

    expertises = Expertise.objects.filter(active=True)

    context = {
        'carousel_first': carousel_first,
        'carousels': carousels,
        'about': about[0],
        'expertises': expertises
    }

    return render(request, 'main/index.html', context )


