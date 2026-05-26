# KworksService

Методы управления кворками пользователя.

## deleteKwork

Удаление кворка.

- **Endpoint:** `/deleteKwork`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.delete_kwork(kwork_id=1)`

## kworksStatusList

Получение списка статусов кворков.

- **Endpoint:** `/kworksStatusList`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_kworks_status_list()`

## markKworkAsFavorite

Отметка кворка как избранного.

- **Endpoint:** `/markKworkAsFavorite`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `is_favorite` (bool) - Флаг избранного
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.mark_kwork_as_favorite(kwork_id=1, is_favorite=True)`

## markKworkAsHidden

Отметка кворка как скрытого.

- **Endpoint:** `/markKworkAsHidden`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `is_hidden` (bool) - Флаг скрытого
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.mark_kwork_as_hidden(kwork_id=1, is_hidden=True)`

## markKworksBlackFriday

Отметка кворка для Black Friday.

- **Endpoint:** `/markKworksBlackFriday`
- **Метод:** POST
- **Параметры:**
  - `kworkId` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.mark_kworks_black_friday(kwork_id=1)`

## pauseKwork

Пауза кворка.

- **Endpoint:** `/pauseKwork`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.pause_kwork(kwork_id=1)`

## setAvailableAtWeekends

Установка доступности в выходные.

- **Endpoint:** `/setAvailableAtWeekends`
- **Метод:** POST
- **Параметры:**
  - `is_available` (bool) - Флаг доступности
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.set_available_at_weekends(is_available=True)`

## startKwork

Запуск кворка.

- **Endpoint:** `/startKwork`
- **Метод:** POST
- **Параметры:**
  - `kwork_id` (int) - ID кворка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.start_kwork(kwork_id=1)`
