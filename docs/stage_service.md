# StageService

Методы для работы с этапами заказа.

## createStage

Создание этапа в заказе.

- **Endpoint:** `/createStage`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `extend_time` (int) - Добавляемое время
  - `stages` (object) - Параметры этапов
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.create_stage(order_id=1, extend_time=1, stages={})`

## addStage

Добавление этапа в заказ.

- **Endpoint:** `/addStage`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `extend_time` (int) - Добавляемое время
  - `stages` (object) - Параметры этапов
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.add_stage(order_id=1, extend_time=1, stages={})`

## orderStage

Резервирование этапа.

- **Endpoint:** `/orderStage`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `stage_id` (int) - ID этапа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.order_stage(order_id=1, stage_id=1)`

## editStage

Редактирование этапа в заказе.

- **Endpoint:** `/editStage`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `extendTime` (int) - Добавляемое время
  - `stages` (object) - Параметры этапов
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.edit_stage(order_id=1, extend_time=1, stages={})`

## updateStageProgress

Обновление прогресса этапа.

- **Endpoint:** `/updateStageProgress`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `stages` (object) - Прогресс этапов
  - `comment` (string) - Комментарий
  - `metrics[]` (array, optional) - ID файлов отчета
  - `trackId` (int, optional) - ID трека
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.update_stage_progress(order_id=1, stages={}, comment="text")`
