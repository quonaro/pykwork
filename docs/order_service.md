# OrderService

Методы для работы с заказами.

## order

Получение заказа по ID.

- **Endpoint:** `/order`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_order(order_id=1)`

## getOrderFiles

Получение файлов заказа.

- **Endpoint:** `/getOrderFiles`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_order_files(order_id=1)`

## getOrderHeader

Получение заголовка заказа.

- **Endpoint:** `/getOrderHeader`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `orderHash` (int, optional) - Хеш заказа
  - `kworkHash` (int, optional) - Хеш кворка
  - `payerHash` (int, optional) - Хеш покупателя
  - `workerHash` (int, optional) - Хеш продавца
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_order_header(order_id=1)`

## getOrderDetails

Получение деталей заказа.

- **Endpoint:** `/getOrderDetails`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_order_details(order_id=1)`

## sendOrderForApproval

Отправка заказа на проверку.

- **Endpoint:** `/sendOrderForApproval`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `metrics[]` (array, optional) - ID файлов отчета
  - `stageIds[]` (array, optional) - ID этапов
  - `filesIds[]` (array, optional) - ID файлов
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.send_order_for_approval(order_id=1)`

## approveOrder

Принятие заказа.

- **Endpoint:** `/approveOrder`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `portfolio` (int) - Разрешение на портфолио (0 или 1)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.approve_order(order_id=1, portfolio=1)`

## approveOrderStage

Принятие этапа заказа.

- **Endpoint:** `/approveOrderStage`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `stageIds[]` (array, optional) - ID этапов
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.approve_order_stage(order_id=1)`

## sendOrderForRevision

Отправка заказа на доработку.

- **Endpoint:** `/sendOrderForRevision`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `revision` (string, optional) - Комментарий
  - `files[]` (array, optional) - ID файлов
  - `stageIds[]` (array, optional) - ID этапов
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.send_order_for_revision(order_id=1, revision="text")`

## sendBonus

Отправка бонуса продавцу.

- **Endpoint:** `/sendBonus`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `bonus` (int) - Сумма бонуса
  - `comment` (string, optional) - Комментарий
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.send_bonus(order_id=1, bonus=100, comment="good work")`

## sendOrderForArbitration

Отправка заказа на арбитраж.

- **Endpoint:** `/sendOrderForArbitration`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `reasonId` (int) - ID причины
  - `comments` (string) - Комментарии
  - `files[]` (array, optional) - ID файлов
  - `stageIds[]` (array, optional) - ID этапов
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.send_order_for_arbitration(order_id=1, reason_id=1, comments="text")`

## getArbitrationReasons

Получение причин арбитража.

- **Endpoint:** `/getArbitrationReasons`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_arbitration_reasons(order_id=1)`

## rateArbitration

Оценка арбитража.

- **Endpoint:** `/rateArbitration`
- **Метод:** POST
- **Параметры:**
  - `id` (int) - ID трека
  - `rating` (int) - Оценка
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.rate_arbitration(id=1, rating=5)`

## cancelOrderAwaitingPayment

Отмена неоплаченного заказа.

- **Endpoint:** `/cancelOrderAwaitingPayment`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.cancel_order_awaiting_payment(order_id=1)`

## payOrderAwaitingPayment

Оплата неоплаченного заказа.

- **Endpoint:** `/payOrderAwaitingPayment`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.pay_order_awaiting_payment(order_id=1)`

## allowOrderPortfolioUpload

Разрешение публикации в портфолио.

- **Endpoint:** `/allowOrderPortfolioUpload`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.allow_order_portfolio_upload(order_id=1)`

## getOrderProvidedData

Получение предоставленных данных заказа.

- **Endpoint:** `/getOrderProvidedData`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_order_provided_data(order_id=1)`

## setOrderRating

Оценка продавца.

- **Endpoint:** `/setOrderRating`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `speed` (int) - Скорость (1-5)
  - `quality` (int) - Качество (1-5)
  - `communication` (int) - Коммуникация (1-5)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.set_order_rating(order_id=1, speed=5, quality=5, communication=5)`

## sendOrderReceiptLinkForVerification

Отправка ссылки на чек.

- **Endpoint:** `/sendOrderReceiptLinkForVerification`
- **Метод:** POST
- **Параметры:**
  - `receiptId` (int) - ID чека
  - `receiptLink` (string) - Ссылка на чек
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.send_order_receipt_link_for_verification(receipt_id=1, receipt_link="https://...")`

## saveOrderNote

Сохранение заметки о заказе.

- **Endpoint:** `/saveOrderNote`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `note` (string) - Текст заметки (body)
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.save_order_note(order_id=1, note="note text")`

## deleteOrderNote

Удаление заметки о заказе.

- **Endpoint:** `/deleteOrderNote`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.delete_order_note(order_id=1)`

## sendOrderRequirements

Отправка требований к заказу.

- **Endpoint:** `/sendOrderRequirements`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `requirements` (string, optional) - Требования
  - `files[]` (array, optional) - ID файлов
  - `metrics[]` (array, optional) - ID метрик
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.send_order_requirements(order_id=1, requirements="text")`

## offerOrderOptions

Предложение опций к заказу.

- **Endpoint:** `/offerOrderOptions`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `options` (object, optional) - Опции
  - `customOptions` (object, optional) - Кастомные опции
  - `updatedPackage` (string, optional) - Обновленный пакет
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.offer_order_options(order_id=1)`

## getExtrasAvailableForOrder

Получение доступных опций заказа.

- **Endpoint:** `/getExtrasAvailableForOrder`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_extras_available_for_order(order_id=1)`

## getOrderedExtras

Получение заказанных опций.

- **Endpoint:** `/getOrderedExtras`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_ordered_extras(order_id=1)`

## getCustomOptionsPresets

Получение пресетов кастомных опций.

- **Endpoint:** `/getCustomOptionsPresets`
- **Метод:** POST
- **Параметры:**
  - `order_id` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_custom_options_presets(order_id=1)`

## getOrderCancellationReasons

Получение причин отмены заказа.

- **Endpoint:** `/getOrderCancellationReasons`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.get_order_cancellation_reasons(order_id=1)`

## orderKwork

Заказ кворка.

- **Endpoint:** `/orderKwork`
- **Метод:** POST
- **Параметры:**
  - `kworkId` (int) - ID кворка
  - `kworksCount` (int, optional) - Количество кворков
  - `volumeTypeId` (int, optional) - ID типа объема
  - `volume` (float, optional) - Объем
  - `packageId` (int, optional) - ID пакета
  - `extras` (object, optional) - Дополнительные опции
  - `channel_format` (string, optional) - Формат размещения
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.order_kwork(kwork_id=1, kworks_count=1, volume=10.0)`

## repeatOrder

Повтор заказа.

- **Endpoint:** `/repeatOrder`
- **Метод:** POST
- **Параметры:**
  - `orderId` (int) - ID заказа
  - `token` (string) - Токен авторизации
- **Метод библиотеки:** `await client.repeat_order(order_id=1)`
