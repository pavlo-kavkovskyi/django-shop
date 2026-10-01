# django-shop

Sklep internetowy w Django – projekt z zajęć, klasa 4 Technik Programista.

## Technologie

- Python 3.12+, Django 6
- SQLite
- Szablony Django, CSS

## Uruchomienie

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Aplikacja: http://127.0.0.1:8000

## Struktura

```text
manage.py          – narzędzie do uruchamiania, migracji, konsoli
config/settings.py – ustawienia projektu
config/urls.py     – główna mapa URL: przekazuje prefiksy do aplikacji
shop/urls.py       – URL-e aplikacji shop (trasy → widoki)
shop/views.py      – widoki (kontrolery z MVC)
```

Są **dwa** pliki `urls.py`: projektowy mówi „ten prefiks obsługuje aplikacja `shop`”
(`include("shop.urls")`), aplikacyjny mówi „ten widok obsługuje tę resztę adresu”.
Dzięki temu aplikację `shop` można wpiąć do innego projektu jedną linią.

## Trasy

| Metoda | Adres | Nazwa trasy | Opis |
|--------|-------|-------------|------|
| GET | `/` | `shop:index` | nazwa projektu |
| GET | `/about/`, `/contact/`, `/terms/` | `shop:about` … | teksty statyczne |
| GET | `/api/info/` | `shop:api_info` | JSON: name, author, version |
| GET | `/admin-panel/` | `shop:admin_panel` | zawsze 403 |
| GET | `/hello/<str:name>/` | `shop:hello` | powitanie |
| GET | `/hello/<str:name>/<int:age>/` | `shop:hello_age` | powitanie z wiekiem |
| GET | `/add/`, `/subtract/`, `/multiply/`, `/divide/` + `<int:a>/<int:b>/` | `shop:add` … | kalkulator; dzielenie przez 0 → 400 |
| GET | `/products/<slug:slug>/` | `shop:product_slug` | slug: litery, cyfry, `-`, `_` |
| GET | `/items/?category=&sort=&page=` | `shop:items` | query string; domyślnie „all, default”; `?page=abc` → strona 1 |
| GET | `/items/<int:item_id>/` | `shop:item_detail` | element ze słownika; brak → 404 |
| GET | `/start/` | `shop:start` | redirect 302 na `/` |
| GET | `/links/` | `shop:links` | adresy zbudowane przez `reverse` |
| GET | `/admin/` | – | panel admina Django |

## Obserwacje z zadań

**Ukośnik (zadanie 4).** `/about` bez ukośnika → Django odpowiada 301 na `/about/`, potem 200
(do sprawdzenia w Network). Po zmianie wzorca na `"about"` Django przestaje dopasowywać `/about/` (404),
a `/about` działa – dlatego trzymamy konwencję „wzorzec z ukośnikiem na końcu”.

**`/add/a/b/` (zadanie 5).** Kod 404 – konwerter `int` nie dopasował `a`, więc trasa nie pasuje
i widok w ogóle się nie wywołuje.

**Slug (zadanie 6).** `/products/laptop-dell-15/` działa (same litery, cyfry i myślniki),
`/products/laptop dell/` ze spacją nie pasuje do `slug` → 404.

**Http404 (zadanie 8).** Przy `DEBUG=True` Django pokazuje żółtą stronę z komunikatem
„Nie ma takiego elementu” i listą wszystkich tras, które próbowało dopasować.

**Brak `app_name` (zadanie 9).** Bez `app_name = "shop"` `redirect("shop:index")` i `reverse("shop:...")`
kończą się `NoReverseMatch: 'shop' is not a registered namespace`.

## Autor

Jan Kowalski, 4TP
