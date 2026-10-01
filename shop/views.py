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
