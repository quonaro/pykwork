# InboxService

Методы управления inbox сообщениями.

## getInboxTracks

Получение inbox треков.

- **Endpoint:** `/getInboxTracks`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_inbox_tracks()`

## inboxTrackMessage

Отправка сообщения трека.

- **Endpoint:** `/inboxTrackMessage`
- **Метод:** POST
- **Параметры:**
  - `track_id` (int) - ID трека
  - `message` (string) - Сообщение
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.inbox_track_message(track_id=1, message="text")`

## inboxComplainMessage

Пожаловаться на сообщение.

- **Endpoint:** `/inboxComplainMessage`
- **Метод:** POST
- **Параметры:**
  - `track_id` (int) - ID трека
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.inbox_complain_message(track_id=1)`

## inboxDelete

Удаление inbox.

- **Endpoint:** `/inboxDelete`
- **Метод:** POST
- **Параметры:**
  - `track_id` (int) - ID трека
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.inbox_delete(track_id=1)`

## inboxEdit

Редактирование inbox.

- **Endpoint:** `/inboxEdit`
- **Метод:** POST
- **Параметры:**
  - `track_id` (int) - ID трека
  - `text` (string) - Текст
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.inbox_edit(track_id=1, text="text")`

## inboxForward

Пересылка inbox.

- **Endpoint:** `/inboxForward`
- **Метод:** POST
- **Параметры:**
  - `track_id` (int) - ID трека
  - `user_id` (int) - ID пользователя
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.inbox_forward(track_id=1, user_id=1)`

## inboxMessage

Отправка inbox сообщения.

- **Endpoint:** `/inboxMessage`
- **Метод:** POST
- **Параметры:**
  - `user_id` (int) - ID пользователя
  - `message` (string) - Сообщение
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.inbox_message(user_id=1, message="text")`

## markInboxTracksAsRead

Отметка inbox треков как прочитанных.

- **Endpoint:** `/markInboxTracksAsRead`
- **Метод:** POST
- **Параметры:**
  - `ids[]` (list) - Список ID треков
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.mark_inbox_tracks_as_read(track_ids=[1, 2, 3])`

## offline

Переход в офлайн.

- **Endpoint:** `/offline`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.inbox_offline()`

## searchMessages

Поиск сообщений.

- **Endpoint:** `/searchMessages`
- **Метод:** POST
- **Параметры:**
  - `query` (string) - Поисковый запрос
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.search_messages(query="text")`

## sendUserStatus

Отправка статуса пользователя.

- **Endpoint:** `/sendUserStatus`
- **Метод:** POST
- **Параметры:**
  - `status` (string) - Статус
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.send_user_status(status="online")`
