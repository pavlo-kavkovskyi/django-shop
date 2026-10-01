from django.http import HttpResponse


def index(request):
    return HttpResponse("django-shop – Sklep 4TP")
