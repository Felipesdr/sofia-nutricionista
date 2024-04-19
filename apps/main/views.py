from django.shortcuts import render
from apps.main.models import Carousel, About, Expertise, Appointment, Article

def index(request):
    carousels = Carousel.objects.filter(active=True)
    carousel_first = carousels[0]
    carousels = carousels[1:]

    #about
    about = About.objects.filter(active=True)[:1]
    about[0].title = f'{about[0].text[:17]}...'

    #expertise
    expertises = Expertise.objects.filter(active=True)

    #appointment
    appointment = Appointment.objects.filter(active=True)

    #article
    articles = Article.objects.filter(active=True)
    first_articles = articles[:3]
    second_articles = articles[3:7]

    context = {
        'carousel_first': carousel_first,
        'carousels': carousels,
        'about': about[0],
        'expertises': expertises,
        'appointment': appointment,
        'first_articles': first_articles,
        'second_articles': second_articles,
        'articles': articles
    }

    return render(request, 'main/index.html', context )

def articles(request):
    articles = Article.objects.filter(active=True)
    return render(request, 'main/articles.html', {'articles': articles})


