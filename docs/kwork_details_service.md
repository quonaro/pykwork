# KworkDetailsService

Методы получения деталей кворков.

## createKworkComplain

Создание жалобы на кворк.

- **Endpoint:** `/createKworkComplain`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `category_id` (int) - ID категории жалобы
  - `text` (string) - Текст жалобы
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.create_kwork_complain(kwork_id=1, category_id=1, text="text")`

## getComplainCategories

Получение категорий жалоб.

- **Endpoint:** `/getComplainCategories`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_complain_categories()`

## getKworkAnswers

Получение FAQ кворка.

- **Endpoint:** `/getKworkAnswers`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_kwork_answers(kwork_id=1)`

## getKworkDetails

Получение деталей кворка.

- **Endpoint:** `/getKworkDetails`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_kwork_details(kwork_id=1)`

## getKworkDetailsExtra

Получение дополнительных деталей кворка.

- **Endpoint:** `/getKworkDetailsExtra`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_kwork_details_extra(kwork_id=1)`

## getKworkLinksTable

Получение таблицы ссылок кворка.

- **Endpoint:** `/getKworkLinksTable`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_kwork_links_table(kwork_id=1)`

## getKworkPortfolios

Получение портфолио кворка.

- **Endpoint:** `/getKworkPortfolios`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_kwork_portfolios(kwork_id=1)`

## getKworkReviews

Получение отзывов кворка.

- **Endpoint:** `/getKworkReviews`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_kwork_reviews(kwork_id=1)`

## orderKwork

Заказ кворка.

- **Endpoint:** `/orderKwork`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - Дополнительные параметры (kwargs)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.order_kwork(kwork_id=1, **kwargs)`

## rechargeBalance

Пополнение баланса.

- **Endpoint:** `/rechargeBalance`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `paymentId` (int) - ID платежа
  - `amount` (int) - Сумма пополнения
  - `paymentType` (string) - Тип платежа
  - `countryGroupCode` (string) - Код страны
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.recharge_balance(order_id=1, payment_id=1, amount=1000, payment_type="card", country_group_code="RU")`
