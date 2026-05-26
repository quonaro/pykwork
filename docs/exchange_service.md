# ExchangeService

Методы биржи проектов (connects).

## myWants

Получение архивных проектов пользователя.

- **Endpoint:** `/myWants`
- **Метод:** POST
- **Параметры:**
  - `page` (int) - Номер страницы
  - `want_status_id` (int) - ID статуса проекта
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_my_wants(page=1, want_status_id=0)`

## deleteOffer

Удаление отклика.

- **Endpoint:** `/deleteOffer`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID отклика
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.delete_offer(offer_id=1)`

## deleteWant

Удаление проекта (want).

- **Endpoint:** `/deleteWant`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID проекта
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.delete_want(want_id=1)`

## exchangeInfo

Получение информации о бирже.

- **Endpoint:** `/exchangeInfo`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_exchange_info()`

## favoriteCategories

Получение избранных категорий.

- **Endpoint:** `/favoriteCategories`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_favorite_categories()`

## offer

Получение конкретного отклика.

- **Endpoint:** `/offer`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID отклика
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_offer(offer_id=1)`

## getWantsCount

Получение количества проектов с фильтрацией.

- **Endpoint:** `/getWantsCount`
- **Метод:** POST
- **Параметры:**
  - `categories` (string) - ID категорий
  - `attributes` (string) - Атрибуты фильтрации
  - `price_from` (int) - Минимальная цена
  - `price_to` (int) - Максимальная цена
  - `hiring_from` (int) - Минимальный процент найма
  - `offers` (string) - Фильтр по откликам
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_wants_count(categories="", attributes="", price_from=0, price_to=0, hiring_from=0, offers="")`

## projects

Получение проектов исполнителя.

- **Endpoint:** `/projects`
- **Метод:** POST
- **Параметры:**
  - `categories` (string) - ID категорий
  - `attributes` (string) - Атрибуты фильтрации
  - `price_from` (int) - Минимальная цена
  - `price_to` (int) - Максимальная цена
  - `hiring_from` (int) - Минимальный процент найма
  - `offers` (string) - Фильтр по откликам
  - `query` (string) - Поисковый запрос
  - `page` (int) - Номер страницы
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_worker_projects(categories="", attributes="", price_from=0, price_to=0, hiring_from=0, offers="", query="", page=1)`

## restartWant

Перезапуск проекта.

- **Endpoint:** `/restartWant`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID проекта
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.restart_want(want_id=1)`

## setFavorite

Установка избранных категорий.

- **Endpoint:** `/setFavorite`
- **Метод:** POST
- **Параметры:**
  - `categories` (string) - ID категорий
  - `attributes` (string) - Атрибуты
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.set_favorite(categories="", attributes="")`

## stopWant

Остановка проекта.

- **Endpoint:** `/stopWant`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID проекта
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.stop_want(want_id=1)`

## wantsStatusList

Получение списка статусов проектов.

- **Endpoint:** `/wantsStatusList`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_wants_status_list()`
