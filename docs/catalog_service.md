# CatalogService

Методы каталога кворков.

## catalogFilters

Получение фильтров каталога.

- **Endpoint:** `/catalogFilters`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_catalog_filters()`

## mainData

Получение основных данных (v1).

- **Endpoint:** `/mainData`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_main_data()`

## mainDataV2

Получение основных данных (v2).

- **Endpoint:** `/mainDataV2`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_main_data_v2()`

## rubrics

Получение рубрик.

- **Endpoint:** `/rubrics`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_rubrics()`

## favoriteKworks

Получение избранных кворков.

- **Endpoint:** `/favoriteKworks`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_favorite_kworks()`

## hiddenKworks

Получение скрытых кворков.

- **Endpoint:** `/hiddenKworks`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_hidden_kworks()`

## generalKworks

Получение общих кворков.

- **Endpoint:** `/generalKworks`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_general_kworks()`

## viewedKworks

Получение просмотренных кворков.

- **Endpoint:** `/viewedKworks`
- **Метод:** POST
- **Параметры:**
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_viewed_kworks()`

## searchKworks

Поиск кворков по запросу.

- **Endpoint:** `/searchKworks`
- **Метод:** POST
- **Параметры:**
  - `query` (string) - Поисковый запрос
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.search_kworks(query="python")`

## searchKworksForUser

Поиск кворков для пользователя.

- **Endpoint:** `/searchKworksForUser`
- **Метод:** POST
- **Параметры:**
  - `query` (string) - Поисковый запрос
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.search_kworks_for_user(query="python")`
