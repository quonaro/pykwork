# OfferService

Методы для работы с откликами.

## offer

Получение отклика по ID.

- **Endpoint:** `/offer`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID отклика
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_offer(id=1)`

## offers

Получение списка откликов.

- **Endpoint:** `/offers`
- **Метод:** POST
- **Параметры:**
  - `page` (int) - Номер страницы
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_offers(page=1)`

## deleteOffer

Удаление отклика.

- **Endpoint:** `/deleteOffer`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID отклика
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.delete_offer(id=1)`
