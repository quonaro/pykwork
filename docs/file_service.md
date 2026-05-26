# FileService

Методы для работы с файлами.

## fileUpload

Загрузка файла.

- **Endpoint:** `/fileUpload`
- **Метод:** POST
- **Параметры:**
  - Файл (multipart/form-data)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.file_upload(file_data)`

## voiceUpload

Загрузка голосового файла.

- **Endpoint:** `/voiceUpload`
- **Метод:** POST
- **Параметры:**
  - Файл (multipart/form-data)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.voice_upload(file_data)`

## fileDelete

Удаление файла.

- **Endpoint:** `/fileDelete`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID файла
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.file_delete(file_id=1)`

## uploadedFile

Получение информации о загруженном файле.

- **Endpoint:** `/uploadedFile`
- **Метод:** POST
- **Параметры:**
  - `path` (string) - Путь к файлу
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.uploaded_file(path="/path/to/file")`

## miniature

Получение миниатюры файла.

- **Endpoint:** `/miniature`
- **Метод:** POST
- **Параметры:**
  - `path` (string) - Путь к файлу
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.miniature(path="/path/to/file")`
