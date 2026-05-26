# TrackService

Методы управления треками сообщений.

## getTracks

Получение треков.

- **Endpoint:** `/getTracks`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `trackId` (int) - ID трека
  - `limit` (int) - Лимит
  - `direction` (string) - Направление
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_tracks(order_id=0, track_id=0, limit=0, direction="")`

## getVoiceMessageTranscription

Получение транскрипции голосового сообщения.

- **Endpoint:** `/getVoiceMessageTranscription`
- **Метод:** POST
- **Параметры:**
  - `conversation_id` (int) - ID беседы
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_voice_message_transcription(conversation_id=1)`

## searchOrderTracks

Поиск треков заказа.

- **Endpoint:** `/searchOrderTracks`
- **Метод:** POST
- **Параметры:**
  - `text` (string) - Текст поиска
  - `orderId` (int) - ID заказа
  - `page` (int) - Номер страницы
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.search_order_tracks(text="query", order_id=1, page=1)`

## inboxCreate

Создание трека.

- **Endpoint:** `/inboxCreate`
- **Метод:** POST
- **Параметры:**
  - `user_id` (int) - ID пользователя
  - `message_key` (string) - Ключ сообщения
  - `text` (string) - Текст
  - `order_id` (int) - ID заказа
  - `uploaded_files[]` (list) - Загруженные файлы
  - `reply_message_id` (int) - ID ответа
  - `withTracks` (int) - Флаг загрузки треков
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.create_track(user_id=1, message_key="key", text="text", order_id=0, uploaded_files=[], reply_message_id=0, with_tracks=0)`

## trackDelete

Удаление трека.

- **Endpoint:** `/trackDelete`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID трека
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.delete_track(track_id=1)`

## trackEdit

Редактирование трека.

- **Endpoint:** `/trackEdit`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID трека
  - `text` (string) - Текст
  - `quoteId` (int) - ID цитаты
  - `uploadedFiles[]` (list) - Загруженные файлы
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.edit_track(track_id=1, text="text", quote_id=0, uploaded_files=[])`
