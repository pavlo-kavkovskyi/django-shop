from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

ITEMS = {
    1: "Laptop",
    2: "Mysz",
    3: "Klawiatura",
    4: "Monitor",
    5: "Słuchawki",
}


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


def product_slug(request, slug):
    return HttpResponse(f"Produkt: {slug}")


def items(request):
    category = request.GET.get("category", "all")
    sort = request.GET.get("sort", "default")
    page_raw = request.GET.get("page", "1")
    # ?page=abc nie może dać 500 – złe dane od klienta to nie błąd serwera
    page = int(page_raw) if page_raw.isdigit() else 1
    return HttpResponse(f"Kategoria: {category}, sortowanie: {sort}, strona: {page}")


def item_detail(request, item_id):
    if item_id not in ITEMS:
        raise Http404("Nie ma takiego elementu")
    return HttpResponse(f"Element: {ITEMS[item_id]}")


def start(request):
    return redirect("shop:index")


def links(request):
    addresses = [
        reverse("shop:index"),
        reverse("shop:about"),
        reverse("shop:hello", args=["Ania"]),
    ]
    return HttpResponse("<br>".join(addresses))
