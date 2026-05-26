# VoiceService

Методы для работы с голосовыми сообщениями.

## getVoiceMessageTranscription

Получение транскрипции голосового сообщения.

- **Endpoint:** `/getVoiceMessageTranscription`
- **Метод:** POST
- **Параметры:**
  - `conversation_id` (int) - ID беседы
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_voice_message_transcription(conversation_id=1)`

## getVoiceMessageConvertStatus

Получение статуса конвертации голосового сообщения.

- **Endpoint:** `/getVoiceMessageConvertStatus`
- **Метод:** POST
- **Параметры:**
  - `file_id` (int) - ID файла
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_voice_message_convert_status(file_id=1)`

## setVoiceMessageSpeed

Установка скорости воспроизведения голосового сообщения.

- **Endpoint:** `/setVoiceMessageSpeed`
- **Метод:** POST
- **Параметры:**
  - `conversation_id` (int) - ID беседы
  - `speed` (float) - Скорость воспроизведения
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.set_voice_message_speed(conversation_id=1, speed=1.5)`

## setVoiceMessageReceiving

Установка статуса получения голосового сообщения.

- **Endpoint:** `/setVoiceMessageReceiving`
- **Метод:** POST
- **Параметры:**
  - `conversation_id` (int) - ID беседы
  - `isReceiving` (int) - Флаг получения (0 или 1)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.set_voice_message_receiving(conversation_id=1, is_receiving=1)`
