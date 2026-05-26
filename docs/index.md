# Kwork API Documentation

Документация по методам API Kwork с указанием endpoints.

## Содержание

- [Авторизация](auth.md) - signIn, actor, user
- [UserService](user_service.md) - Управление пользователями
- [ExchangeService](exchange_service.md) - Биржа проектов
- [DialogService](dialog_service.md) - Диалоги и сообщения
- [CatalogService](catalog_service.md) - Каталог кворков
- [KworkDetailsService](kwork_details_service.md) - Детали кворков
- [KworksService](kworks_service.md) - Управление кворками
- [InboxService](inbox_service.md) - Inbox сообщения
- [TrackService](track_service.md) - Треки сообщений
- [NotificationService](notification_service.md) - Уведомления

## Дополнительная документация

- [API Endpoints](api_endpoints.md) - Полный список endpoints
- [API Documentation](API_DOCUMENTATION.md) - Подробная документация API с примерами

## Базовая информация

- **Base URL:** `https://api.kwork.ru`
- **HTTP метод:** POST
- **Content-Type:** application/json
- **Authorization:** Basic Auth (mobile_api:qFvfRl7w)

## Общие параметры

| Параметр | Описание |
|----------|----------|
| token | Токен авторизации пользователя |
| uad | Уникальный идентификатор устройства |
| device | Модель устройства |
| slrememberme | Cookie для запоминания сессии |
