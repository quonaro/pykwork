# PaymentService

Методы для работы с платежами.

## getPaymentMethods

Получение доступных методов оплаты.

- **Endpoint:** `/getPaymentMethods`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_payment_methods()`

## getBillRefillUrl

Получение URL для пополнения баланса.

- **Endpoint:** `/getBillRefillUrl`
- **Метод:** POST
- **Параметры:**
  - `amount` (int) - Сумма пополнения
  - `paymentType` (string) - Тип платежа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_bill_refill_url(amount=1000, payment_type="card")`
