# DialogService

Методы управления диалогами.

## hideDialog

Скрытие/восстановление диалога.

- **Endpoint:** `/hideDialog`
- **Метод:** POST
- **Параметры:**
  - `userId` (int) - ID пользователя
  - `isRestore` (int) - Флаг восстановления (0 или 1)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.hide_dialog(user_id=1, is_restore=0)`

## dialogs

Получение списка диалогов.

- **Endpoint:** `/dialogs`
- **Метод:** POST
- **Параметры:**
  - `page` (int) - Номер страницы
  - `filter` (string) - Фильтр
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_dialogs(page=1, filter_str="")`

## getDialog

Получение конкретного диалога.

- **Endpoint:** `/getDialog`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID диалога
  - `withTracks` (int) - Флаг загрузки треков (0 или 1)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_dialog(dialog_id=1, with_tracks=0)`

## getFishingTutorialQuestions

Получение вопросов викторины.

- **Endpoint:** `/getFishingTutorialQuestions`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_quiz_questions()`

## inboxRead

Отметка диалога как прочитанного.

- **Endpoint:** `/inboxRead`
- **Метод:** POST
- **Параметры:**
  - `user_id` (int) - ID пользователя
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.mark_dialog_read(user_id=1)`

## setFishingTutorialStatus

Установка статуса викторины.

- **Endpoint:** `/setFishingTutorialStatus`
- **Метод:** POST
- **Параметры:**
  - `status` (int) - Статус
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.set_quiz_status(status=1)`

## setDialogStarred

Отметка диалога как избранного.

- **Endpoint:** `/setDialogStarred`
- **Метод:** POST
- **Параметры:**
  - `userId` (int) - ID пользователя
  - `isStarred` (int) - Флаг избранного (0 или 1)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.set_dialog_starred(user_id=1, is_starred=1)`

## unreadDialog

Отметка диалога как непрочитанного.

- **Endpoint:** `/unreadDialog`
- **Метод:** POST
- **Параметры:**
  - `user_id` (int) - ID пользователя
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.mark_dialog_unread(user_id=1)`
