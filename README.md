# Aplikacja z prostym modelem ML

Aplikacja API w Flasku, która przyjmuje dwie liczby i zwraca predykcję na podstawie ich sumy.

# Endpoint

- **GET** `/api/v1.0/predict`

# Parametry (w URL):

- `num1` – pierwsza liczba
- `num2` – druga liczba

# Przykład żądania

http://127.0.0.1:5000/api/v1.0/predict?num1=3.5&num2=3

# Przykład odpowiedzi

#### Przykładowa odpowiedź:
```json
{
  "features": {
    "num1": 3.5,
    "num2": 3.0
  },
  "prediction": 1
}
```
# Uruchomienie w Dockerze

```bash
docker build -t api-ml .
docker run -p 5000:5000 api-ml
```
