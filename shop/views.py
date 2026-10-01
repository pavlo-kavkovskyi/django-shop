from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("django-shop – Sklep 4TP")


def about(request):
    return HttpResponse("Jesteśmy klasą 4TP. Robimy sklep internetowy.")


def contact(request):
    return HttpResponse("Napisz: sklep@example.com")


def terms(request):
    return HttpResponse("Regulamin sklepu: kupujesz, płacisz, odbierasz. Zwrot w 14 dni.")


def api_info(request):
    return JsonResponse({"name": "django-shop", "author": "Jan Kowalski", "version": "0.1"})


def admin_panel(request):
    return HttpResponse("Brak dostępu", status=403)


def hello(request, name):
    return HttpResponse(f"Cześć, {name}!")


def hello_age(request, name, age):
    return HttpResponse(f"Cześć, {name}, masz {age} lat")


def add(request, a, b):
    return HttpResponse(f"{a} + {b} = {a + b}")


def subtract(request, a, b):
    return HttpResponse(f"{a} - {b} = {a - b}")


def multiply(request, a, b):
    return HttpResponse(f"{a} * {b} = {a * b}")


def divide(request, a, b):
    if b == 0:
        return HttpResponse("Nie dzielimy przez zero", status=400)
    return HttpResponse(f"{a} / {b} = {a / b}")
