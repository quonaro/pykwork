# UserService

Методы управления пользователями и диалогами.

## userByUsername

Получение пользователя по username.

- **Endpoint:** `/userByUsername`
- **Метод:** POST
- **Параметры:**
  - `username` (string) - Имя пользователя
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_user_by_username(username="username")`

## userKworks

Получение кворков пользователя.

- **Endpoint:** `/userKworks`
- **Метод:** POST
- **Параметры:**
  - `user_id` (int) - ID пользователя
  - `page` (int) - Номер страницы
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_user_kworks(user_id=1, page=1)`

## kworksCategoriesList

Получение категорий пользователя.

- **Endpoint:** `/kworksCategoriesList`
- **Метод:** POST
- **Параметры:**
  - `user_id` (int) - ID пользователя
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_user_categories(user_id=1)`

## userReviews

Получение отзывов пользователя.

- **Endpoint:** `/userReviews`
- **Метод:** POST
- **Параметры:**
  - `user_id` (int) - ID пользователя
  - `page` (int) - Номер страницы
  - `type` (string) - Тип отзывов
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_user_reviews(user_id=1, page=1, review_type="")`

## blockDialog

Блокировка диалога с пользователем.

- **Endpoint:** `/blockDialog`
- **Метод:** POST
- **Параметры:**
  - `blockUserId` (int) - ID пользователя для блокировки
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.block_dialog(block_user_id=1)`

## unblockDialog

Разблокировка диалога с пользователем.

- **Endpoint:** `/unblockDialog`
- **Метод:** POST
- **Параметры:**
  - `blockUserId` (int) - ID пользователя для разблокировки
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.unblock_dialog(block_user_id=1)`
