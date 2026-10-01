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
shop/forms.py      – formularze: opis pól + walidacja
shop/templates/shop/ – szablony (base.html, index.html, product_*.html)
shop/static/shop/    – CSS
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

### Dlaczego `shop` dwa razy: `templates/shop/` i `static/shop/`

Django zbiera szablony i pliki statyczne ze **wszystkich** aplikacji do jednej puli.
Gdyby `shop` i `blog` miały po `index.html`, wygrałby ten z aplikacji wyżej w `INSTALLED_APPS`
– po cichu, bez błędu. Podfolder z nazwą aplikacji robi z tego `shop/index.html` i `blog/index.html`.

## Trasy – materiał 11

| Metoda | Adres | Nazwa trasy | Opis |
|--------|-------|-------------|------|
| GET | `/products/` | `shop:product_list` | lista + wyszukiwarka (`?q=`, `?only_available=on`) |
| GET/POST | `/products/add/` | `shop:product_add` | formularz z walidacją; po POST redirect |
| GET | `/products/<int:product_id>/` | `shop:product_detail` | szczegóły; brak → 404 |

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

## Przepisanie `product_list.html` z Jinja2 na DTL (zadanie 3, materiał 11)

Zmienione miejsca – **7**:

| # | Flask (Jinja2) | Django (DTL) |
|---|----------------|--------------|
| 1 | `{{ url_for('product_detail', product_id=p.id) }}` | `{% url 'shop:product_detail' p.id %}` |
| 2 | `{{ url_for('product_add') }}` | `{% url 'shop:product_add' %}` |
| 3 | `{{ loop.index }}` | `{{ forloop.counter }}` |
| 4 | `{{ p.gross_price() }}` (wywołanie metody) | usunięte – w DTL bez nawiasów i bez arytmetyki; liczyć trzeba w modelu |
| 5 | `{{ p.category.name if p.category else '–' }}` (if w wyrażeniu) | `{{ p.category }}` (kategoria to na razie napis) |
| 6 | `{{ p.price }}` | `{{ p.price\|floatformat:2 }}` (filtr z argumentem po dwukropku) |
| 7 | formularz `delete` z `url_for` | usunięty (brak jeszcze usuwania); formularze POST wymagają `{% csrf_token %}` |

## CSRF (zadanie 7)

Atak CSRF polega na tym, że obca strona wysyła w moim imieniu formularz POST do serwisu, w którym jestem zalogowany,
a przeglądarka dołącza moje ciasteczka. Token CSRF to losowa wartość zapisana w ciasteczku i w ukrytym polu formularza,
które muszą się zgadzać; obca strona jej nie zna, więc Django odrzuca żądanie kodem 403.

## Wyszukiwarka bez tokena (zadanie 8)

Formularz wyszukiwania używa GET i nie zmienia danych, więc nie ma czego podrabiać – token CSRF jest potrzebny tylko
przy żądaniach, które zmieniają dane (POST, PUT, PATCH, DELETE). Po wysłaniu pola zostają wypełnione, bo formularz jest
związany z `request.GET`.

## Autor

Jan Kowalski, 4TP
