# pykwork

![Python](https://img.shields.io/badge/python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/pykwork?color=blue&label=pypi&style=flat-square)
![Downloads](https://img.shields.io/pypi/dm/pykwork?color=green&label=downloads&style=flat-square)

> **⚠️ Disclaimer:** Это неофициальная библиотека для работы с API Kwork. Она не аффилирована с компанией Kwork и не является официальным SDK. Используйте на свой риск.

Python библиотека для работы с API Kwork (kwork.ru) с поддержкой async и sync режимов.

**API Documentation:** [https://api.kwork.ru/](https://api.kwork.ru/) (OpenAPI schema)

**API Basic Auth Credentials:**
- Username: `mobile_api`
- Password: `qFvfRl7w`

**Документация по API endpoints:** [docs/](docs/)

## Установка

```bash
# Через PyPI (рекомендуется)
pip install pykwork

# Или через git+
pip install git+https://github.com/quonaro/pykwork.git
```

## Зависимости

```bash
# httpx установится автоматически через uv
# Или вручную:
pip install httpx>=0.24.0
```

## Быстрый старт

### Async (рекомендуется)

```python
import asyncio
from pykwork import KworkClient

async def main():
    async with KworkClient(username="user@email.com", password="password") as client:
        # Авторизация
        await client.login()
        
        # Получение информации о текущем пользователе
        actor = await client.get_actor()
        print(f"User: {actor['response']['username']}")
        
        # Получение проектов
        projects = await client.get_all_projects(max_pages=2)
        print(f"Projects: {len(projects)}")
        
        # Получение откликов
        offers = await client.get_all_offers()
        print(f"Offers: {len(offers)}")

asyncio.run(main())
```

### Sync

```python
from pykwork import KworkSyncClient

with KworkSyncClient(username="user@email.com", password="password") as client:
    # Авторизация
    client.login()
    
    # Получение информации о текущем пользователе
    actor = client.get_actor()
    print(f"User: {actor['response']['username']}")
    
    # Получение проектов
    projects = client.get_all_projects(max_pages=2)
    print(f"Projects: {len(projects)}")
    
    # Получение откликов
    offers = client.get_all_offers()
    print(f"Offers: {len(offers)}")
```

## Основные методы

**Примечание:** Для async клиента используйте `await`, для sync - без `await`.

### Авторизация

```python
# Async
await client.login()

# Sync
client.login()
```

### Пользователи (UserService)

```python
# Async
actor = await client.get_actor()
user = await client.get_user(user_id=1)
user = await client.get_user_by_username(username="username")
kworks = await client.get_user_kworks(user_id=1, page=1)
categories = await client.get_user_categories(user_id=1)
reviews = await client.get_user_reviews(user_id=1, page=1)
await client.block_dialog(block_user_id=1)
await client.unblock_dialog(block_user_id=1)
last_order = await client.get_users_last_order_info(interlocutor_id=1)
orders = await client.orders_between(user_id=1)

# Sync
actor = client.get_actor()
user = client.get_user(user_id=1)
user = client.get_user_by_username(username="username")
kworks = client.get_user_kworks(user_id=1, page=1)
categories = client.get_user_categories(user_id=1)
reviews = client.get_user_reviews(user_id=1, page=1)
client.block_dialog(block_user_id=1)
client.unblock_dialog(block_user_id=1)
last_order = client.get_users_last_order_info(interlocutor_id=1)
orders = client.orders_between(user_id=1)
```

### Диалоги (DialogService)

```python
# Скрыть/восстановить диалог
await client.hide_dialog(user_id=1, is_restore=0)

# Архивировать/разархивировать диалог
await client.archive_dialog(user_id=1)
await client.unarchive_dialog(user_id=1)

# Список диалогов
dialogs = await client.get_dialogs(page=1, filter_str="")

# Поиск диалогов
dialogs = await client.search_dialogs(query="test", page=1)

# Конкретный диалог
dialog = await client.get_dialog(dialog_id=1, with_tracks=0)

# Проверка разрешения диалога
allowed = await client.is_dialog_allow(user_id=1)

# Список заблокированных диалогов
blocked = await client.blocked_dialog_list()
blocked_dialogs = await client.blocked_dialogs()

# Разрешение/отклонение inbox запроса
await client.allow_inbox_request(inbox_id=1, is_accept=1)
await client.inbox_custom_request_decline(message_id=1)
await client.inbox_payer_decline(message_id=1)
await client.inbox_worker_decline(message_id=1)

# Отправка индикатора печати
await client.typing(recipient_id=1, order_id=1)

# Вопросы викторины
questions = await client.get_quiz_questions()

# Отметить диалог как прочитанный
await client.mark_dialog_read(user_id=1)

# Установить статус викторины
await client.set_quiz_status(status=1)

# Отметить диалог как избранный
await client.set_dialog_starred(user_id=1, is_starred=1)

# Отметить диалог как непрочитанный
await client.mark_dialog_unread(user_id=1)
```

### Проекты (ExchangeService)

```python
# Получение проектов (с пагинацией)
projects = await client.get_all_projects(max_pages=5)

# Получение проектов с фильтрацией по категории
it_projects = await client.get_all_projects(categories="11")

# Получение проектов с фильтрацией по цене
cheap_projects = await client.get_all_projects(price_to=1000)

# Получение одной страницы
projects = await client.get_projects(page=1)

# Мои проекты (wants)
wants = await client.get_my_wants(page=1, want_status_id=0)

# Удалить отклик
await client.delete_offer(offer_id=1)

# Удалить проект
await client.delete_want(want_id=1)

# Информация о бирже
info = await client.get_exchange_info()

# Избранные категории
fav_cats = await client.get_favorite_categories()

# Конкретный отклик
offer = await client.get_offer(offer_id=1)

# Количество проектов
count = await client.get_wants_count(categories="11", price_to=1000)

# Проекты исполнителя
worker_projects = await client.get_worker_projects(categories="11", page=1)

# Перезапустить проект
await client.restart_want(want_id=1)

# Установить избранное
await client.set_favorite(categories="11", attributes="")

# Остановить проект
await client.stop_want(want_id=1)

# Статусы проектов
statuses = await client.get_wants_status_list()
```

### Категории (CatalogService)

```python
# Получение списка категорий
categories = await client.get_categories()

# Фильтры каталога
filters = await client.get_catalog_filters(category_id=1, query="test")

# Основные данные (v1)
main_data = await client.get_main_data()

# Основные данные (v2)
main_data_v2 = await client.get_main_data_v2()

# Каталог основные данные
catalog_main = await client.catalog_main()
catalog_main_v2 = await client.catalog_main_v2()

# Рубрики
rubrics = await client.get_rubrics()
catalog_rubrics = await client.catalog_rubrics()

# Категории рубрики
catalog_categories = await client.catalog_categories(rubric_id=1)

# Языки перевода
languages = await client.translation_languages()

# Атрибуты категории
attributes = await client.category_attributes(category_id=1)

# Количество положительных отзывов
count = await client.positive_reviews_count(category_id=1)

# Города и страны
cities = await client.cities()
countries = await client.countries()

# URL модальной компании
url = await client.payer_company_modal_url()

# Избранные кворки
fav_kworks = await client.get_favorite_kworks()

# Скрытые кворки
hidden_kworks = await client.get_hidden_kworks()

# Общие кворки
general_kworks = await client.get_general_kworks()

# Просмотренные кворки
viewed_kworks = await client.get_viewed_kworks()

# Поиск кворков
kworks = await client.search_kworks(query="python")

# Поиск кворков для пользователя
kworks = await client.search_kworks_for_user(query="python")
```

### Отклики

```python
# Получение всех откликов (с пагинацией)
offers = await client.get_all_offers()

# Получение одной страницы
offers = await client.get_offers(page=1)
```

### Кворки (KworkDetailsService)

```python
# Создать жалобу на кворк
await client.create_kwork_complain(kwork_id=1, category_id=1, text="text")

# Категории жалоб
categories = await client.get_complain_categories()

# FAQ кворка
answers = await client.get_kwork_answers(kwork_id=1)

# Детали кворка
details = await client.get_kwork_details(kwork_id=1)

# Дополнительные детали кворка
details_extra = await client.get_kwork_details_extra(kwork_id=1)

# Таблица ссылок кворка
links = await client.get_kwork_links_table(kwork_id=1)

# Портфолио кворка
portfolios = await client.get_kwork_portfolios(kwork_id=1)

# Отзывы кворка
reviews = await client.get_kwork_reviews(kwork_id=1)

# Заказать кворк
await client.order_kwork(kwork_id=1, kworks_count=1, volume=10.0)

# Пополнить баланс
await client.recharge_balance(order_id=1, payment_id=1, amount=1000, payment_type="card", country_group_code="RU")
```

### Кворки пользователя (KworksService)

```python
# Удалить кворк
await client.delete_kwork(kwork_id=1)

# Статусы кворков
statuses = await client.get_kworks_status_list()

# Отметить кворк как избранный
await client.mark_kwork_as_favorite(kwork_id=1, is_favorite=True)

# Отметить кворк как скрытый
await client.mark_kwork_as_hidden(kwork_id=1, is_hidden=True)

# Отметить кворк для Black Friday
await client.mark_kworks_black_friday(kwork_id=1)

# Пауза кворка
await client.pause_kwork(kwork_id=1)

# Доступность в выходные
await client.set_available_at_weekends(is_available=True)

# Запустить кворк
await client.start_kwork(kwork_id=1)
```

### Inbox (InboxService)

```python
# Получить inbox треки
tracks = await client.get_inbox_tracks(username="test", page=1)

# Получить inbox сообщения
inboxes = await client.inboxes(username="test", page="1")

# Получить сообщение трека по conversation ID
track = await client.inbox_track_message(conversation_id=1)

# Пожаловаться на сообщение
await client.inbox_complain_message(message_id=1, complain_category_id=1, comment="text")

# Удалить inbox
await client.inbox_delete(id=1, with_tracks=0)

# Редактировать inbox
await client.inbox_edit(id=1, text="text", uploaded_files={}, reply_message_id=1)

# Переслать inbox
await client.inbox_forward(user_id=1, message_ids=[1, 2])

# Создать inbox сообщение
await client.inbox_create(user_id=1, text="text", uuid="uuid", order_id=1, uploaded_files=[1, 2])

# Получить inbox сообщение по ID
message = await client.inbox_message(message_id=1)

# Отметить inbox треки как прочитанные
await client.mark_inbox_tracks_as_read(user_id=1, conversation_ids=[1, 2, 3])

# Поиск inbox
inboxes = await client.search_inboxes(query="test", user_id=1, page=1)

# Поиск сообщений
messages = await client.search_messages(text="text", user_id=1, page=1)

# Отметить inbox как прочитанный
await client.inbox_read(user_id=1, messages=[1, 2])

# Отправить статус пользователя
await client.send_user_status(user_id=1, status="online", order_id=1)

# Отметить голосовое сообщение как прослушанное
await client.mark_voice_message_heard(conversation_id=1)

# Обновить черновик чата
await client.update_chat_draft_message(user_id=1, message="text", files=[1, 2])
```

### Треки (TrackService)

```python
# Получить треки
tracks = await client.get_tracks(order_id=1, track_id=1, limit=10)

# Транскрипция голосового сообщения
transcription = await client.get_voice_message_transcription(conversation_id=1)

# Поиск треков заказа
tracks = await client.search_order_tracks(text="query", order_id=1, page=1)

# Создать трек
await client.create_track(
    user_id=1,
    message_key="key",
    text="text",
    order_id=1,
    uploaded_files=[],
    reply_message_id=1,
    with_tracks=0
)

# Удалить трек
await client.delete_track(track_id=1)

# Редактировать трек
await client.edit_track(track_id=1, text="text", quote_id=1, uploaded_files=[])
```

### Уведомления (NotificationService)

```python
# Получить уведомления
notifications = await client.get_notifications()

# Отметить уведомления как полученные
await client.notifications_received(ids=[1, 2, 3])

# Получить непрочитанные push события
events = await client.notifications_fetch(page=1, uad="test")

# Валидировать push событие
await client.validate_event(id=1)

# Получить in-app уведомление
notification = await client.get_in_app_notification(uad="test", os_type="ios", os_version="15.0", app_version="2.0")

# Логировать in-app уведомление
await client.push_in_app_notification_log(notification_id=1, action=1)
```

### Файлы (FileService)

```python
# Загрузить файл
await client.file_upload(file_data)

# Загрузить голосовой файл
await client.voice_upload(file_data)

# Удалить файл
await client.file_delete(file_id=1)

# Получить информацию о загруженном файле
file = await client.uploaded_file(path="/path/to/file")

# Получить миниатюру файла
miniature = await client.miniature(path="/path/to/file")
```

### Заказы (OrderService)

```python
# Получить заказ
order = await client.get_order(order_id=1)

# Получить файлы заказа
files = await client.get_order_files(order_id=1)

# Получить заголовок заказа
header = await client.get_order_header(order_id=1)

# Получить детали заказа
details = await client.get_order_details(order_id=1)

# Отправить на проверку
await client.send_order_for_approval(order_id=1)

# Принять заказ
await client.approve_order(order_id=1, portfolio=1)

# Принять этап
await client.approve_order_stage(order_id=1)

# Отправить на доработку
await client.send_order_for_revision(order_id=1, revision="text")

# Отправить бонус
await client.send_bonus(order_id=1, bonus=100, comment="good work")

# Отправить на арбитраж
await client.send_order_for_arbitration(order_id=1, reason_id=1, comments="text")

# Получить причины арбитража
reasons = await client.get_arbitration_reasons(order_id=1)

# Оценить арбитраж
await client.rate_arbitration(id=1, rating=5)

# Отменить неоплаченный заказ
await client.cancel_order_awaiting_payment(order_id=1)

# Оплатить неоплаченный заказ
await client.pay_order_awaiting_payment(order_id=1)

# Разрешить публикацию в портфолио
await client.allow_order_portfolio_upload(order_id=1)

# Получить предоставленные данные
data = await client.get_order_provided_data(order_id=1)

# Оценить продавца
await client.set_order_rating(order_id=1, speed=5, quality=5, communication=5)

# Отправить ссылку на чек
await client.send_order_receipt_link_for_verification(receipt_id=1, receipt_link="https://...")

# Сохранить заметку
await client.save_order_note(order_id=1, note="note text")

# Удалить заметку
await client.delete_order_note(order_id=1)

# Отправить требования
await client.send_order_requirements(order_id=1, requirements="text")

# Предложить опции
await client.offer_order_options(order_id=1)

# Получить доступные опции
extras = await client.get_extras_available_for_order(order_id=1)

# Получить заказанные опции
ordered = await client.get_ordered_extras(order_id=1)

# Получить пресеты кастомных опций
presets = await client.get_custom_options_presets(order_id=1)

# Получить причины отмены
reasons = await client.get_order_cancellation_reasons(order_id=1)

# Повторить заказ
await client.repeat_order(order_id=1)
```

### Платежи (PaymentService)

```python
# Получить методы оплаты
methods = await client.get_payment_methods()

# Получить URL для пополнения
url = await client.get_bill_refill_url(amount=1000, payment_type="card")
```

### Отзывы (ReviewService)

```python
# Создать ответ на отзыв
await client.create_answer(review_id=1, text="response text")

# Редактировать ответ
await client.edit_answer(answer_id=1, text="updated text")
```

### Голосовые сообщения (VoiceService)

```python
# Получить транскрипцию
transcription = await client.get_voice_message_transcription(conversation_id=1)

# Получить статус конвертации
status = await client.get_voice_message_convert_status(file_id=1)

# Установить скорость воспроизведения
await client.set_voice_message_speed(conversation_id=1, speed=1.5)

# Установить статус получения
await client.set_voice_message_receiving(conversation_id=1, is_receiving=1)
```

### Этапы заказа (StageService)

```python
# Создать этап
await client.create_stage(order_id=1, extend_time=1, stages={})

# Добавить этап
await client.add_stage(order_id=1, extend_time=1, stages={})

# Резервировать этап
await client.order_stage(order_id=1, stage_id=1)

# Редактировать этап
await client.edit_stage(order_id=1, extend_time=1, stages={})

# Обновить прогресс этапа
await client.update_stage_progress(order_id=1, stages={}, comment="text")
```

### Отклики (OfferService)

```python
# Получить отклик
offer = await client.get_offer(id=1)

# Получить список откликов
offers = await client.get_offers(page=1)

# Удалить отклик
await client.delete_offer(id=1)
```

## Структура библиотеки

```
pykwork/
├── pyproject.toml          # Конфигурация пакета
├── LICENSE                 # Лицензия (MIT)
├── README.md               # Документация
├── example_async.py        # Пример использования
├── example_sync.py         # Пример использования (sync)
└── pykwork/
    ├── __init__.py         # Экспорт классов
    ├── client.py           # Основной async клиент
    ├── sync_client.py      # Основной sync клиент
    ├── exceptions.py       # Исключения
    ├── logger.py           # Настройка логирования
    └── services/           # Сервисы по категориям
        ├── __init__.py
        ├── user.py         # UserService методы
        ├── dialog.py       # DialogService методы
        ├── exchange.py     # ExchangeService методы
        ├── catalog.py      # CatalogService методы
        ├── kwork.py        # KworkDetailsService методы
        ├── kworks.py       # KworksService методы
        ├── inbox.py        # InboxService методы
        ├── track.py        # TrackService методы
        ├── notification.py # NotificationService методы
        ├── file.py         # FileService методы
        ├── order.py        # OrderService методы
        ├── payment.py      # PaymentService методы
        ├── review.py       # ReviewService методы
        ├── voice.py        # VoiceService методы
        ├── stage.py        # StageService методы
        └── offer.py        # OfferService методы
```

## Исключения

- `KworkAuthError` - Ошибка авторизации
- `KworkRequestError` - Ошибка запроса API

## Пример обработки ошибок

```python
import asyncio
from pykwork import KworkClient, KworkAuthError, KworkRequestError

async def main():
    async with KworkClient(username="user@email.com", password="password") as client:
        try:
            await client.login()
            projects = await client.get_all_projects()
        except KworkAuthError as e:
            print(f"Auth failed: {e}")
        except KworkRequestError as e:
            print(f"Request failed: {e}")
            print(f"Status code: {e.status_code}")

asyncio.run(main())
```

## Конфигурация

```python
client = KworkClient(
    username="user@email.com",
    password="password",
    uad="unique_device_id",  # Уникальный ID устройства
    device="device_model",    # Модель устройства
    timeout=10,                # Таймаут запросов (секунды)
    log_level=30               # Уровень логирования (WARNING по умолчанию)
)
```

## Категории проектов

| ID | Название |
|----|----------|
| 15 | Дизайн |
| 11 | Разработка и IT |
| 5 | Тексты и переводы |
| 17 | SEO и трафик |
| 45 | Соцсети и маркетинг |
| 7 | Аудио, видео, съемка |
| 83 | Бизнес и жизнь |

## Запуск примера

```bash
cd /srv/projects/my/pykwork

# Async пример
uv run python example_async.py

# Sync пример
uv run python example_sync.py
```

## Логирование

Библиотека использует модуль `logging` с уровнем WARNING по умолчанию. Для изменения уровня:

```python
import logging
from pykwork import KworkClient

# Установить уровень DEBUG
client = KworkClient(
    username="user@email.com",
    password="password",
    log_level=logging.DEBUG
)
```

## Лицензия

MIT License
