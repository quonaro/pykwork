# ReviewService

Методы для работы с отзывами и ответами.

## createAnswer

Создание ответа на отзыв.

- **Endpoint:** `/createAnswer`
- **Метод:** POST
- **Параметры:**
  - `review_id` (int) - ID отзыва
  - `text` (string) - Текст ответа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.create_answer(review_id=1, text="response text")`

## editAnswer

Редактирование ответа на отзыв.

- **Endpoint:** `/editAnswer`
- **Метод:** POST
- **Параметры:**
  - `answer_id` (int) - ID ответа
  - `text` (string) - Текст ответа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.edit_answer(answer_id=1, text="updated text")`
