# Статический анализ Android APK 1.90.2

Источник: локальный файл `ru.urentbike.app_1902_rs.apk`.

Сырые файлы APK, декомпилированный код и приватные значения не добавлены в репозиторий. В документацию перенесены только безопасные признаки: host, путь, предполагаемый HTTP-метод и имя клиентского репозитория, где путь встречался.

## Сводка

- SHA-256 APK: `00669a08f8f08e5c152f008d22281681bc38399b0b2dcbbf5acb6e91bccd8d02`
- Инструмент: `jadx`
- Декомпиляция завершилась с частичными ошибками, но строковые константы и имена репозиториев доступны.
- Найдено 123 Urent-связанных path-строки после фильтрации сторонних SDK.
- В `openapi.yaml` добавлено 43 операции со статусом "требует подтверждения трафиком".
- После обновления спецификация содержит 110 операций.

## Основные host

- `app.urentbike.ru`
- `service.urentbike.ru`
- `backyard.urentbike.ru`
- `lg.service.urentbike.ru`
- `notification.service.urentbike.ru`
- `lg.dev.urent.ru`
- `lg.rc.urent.tech`
- `service.jetscooters.fun`

## Добавлено в OpenAPI

Эти операции найдены в клиентских repository-классах. Метод выведен по имени метода клиента и REST-семантике, поэтому параметры и схемы ответов нужно уточнять по реальному трафику.

### Аренда

- `POST /v1/booking/make`
- `POST /v1/booking/cancel`
- `POST /v1/order/cancel`
- `GET /v1/orders/my`
- `GET /v1/orders/my/{order_id}`
- `POST /v1/scooters/openlock/{scooter_id}`
- `POST /v1/scooters/closelock/{scooter_id}`

### Транспорт и зоны

- `GET /v6/transports/polygon`
- `GET /v3/zones/lowspeed/{zone_id}`
- `GET /v1/cities/by_coordinates`

### Подписки и пакеты

- `POST /v1/customerMinutePass/buy`
- `POST /v1/customerMinutePass/buyByAps`
- `POST /v1/customerMinutePass/buyWithUltraDiscount`
- `GET /v1/minutePass/bySpecOffer/{offer_id}`
- `POST /v1/CustomerDailyPass/buy`
- `GET /v1/abonements`
- `GET /v1/dailyPass/available`
- `POST /v1/subscriptions/buy`
- `POST /v1/subscriptions/cancel`
- `POST /v1/subscriptions/change_period`
- `POST /v1/subscriptions/renew`

### Платежи и бонусы

- `POST /v1/pix/create`
- `GET /v1/pix/check-status/{payment_id}`
- `GET /v1/pix/get-last-payments`
- `POST /v1/qpay/links`
- `GET /v1/qpay/check-status/{payment_id}`
- `POST /v1/payme/check-payment`
- `POST /v1/payme/create-payment-url`
- `GET /v1/bonuses/packets`
- `POST /v1/profile/repaydebt`
- `POST /v2/bonuses/purchase`

### Авторизация

- `POST /v2/mobile/code`
- `POST /v1/mobile/mtsid`
- `POST /v1/mobile/mtsidtoken`
- `POST /v1/mobile/mtsidverification`
- `POST /v1/mobile/mosidverification`
- `POST /v1/mosid/sync`

### Повербанки

- `POST /powerbank/v1/order/make`
- `GET /powerbank/v1/station`

### Профиль и обратная связь

- `GET /v1/profile/customInfoBar`
- `GET /v1/profile/season-results`
- `POST /v1/userproblems`
- `POST /v1/vehiclefeedback`

## Найдено, но не добавлено как отдельные операции

Эти пути уже были покрыты спецификацией, требуют дополнительного подтверждения метода, относятся к внешним webview/callback-сценариям или пока оставлены только как инвентарь.

- `/powerbank/v1/activity`
- `/powerbank/v1/models`
- `/powerbank/v1/nearest`
- `/powerbank/v1/stations`
- `/v1/CustomerDailyPass/my`
- `/v1/advertising/preset`
- `/v1/appsflyer/devices`
- `/v1/aps/withdrawal`
- `/v1/bepaid/addcard/webview`
- `/v1/bepaidstripe/addcard/webview`
- `/v1/bikes/bytracker/`
- `/v1/cards/`
- `/v1/cards/cards/`
- `/v1/cards/withPendings`
- `/v1/cities`
- `/v1/cloudpayments/addcard/aps`
- `/v1/cloudpayments/card`
- `/v1/cloudpayments/post3ds`
- `/v1/connect/token`
- `/v1/customerAbonements/my`
- `/v1/customerMinutePass/my`
- `/v1/deletemy`
- `/v1/devices/my/token`
- `/v1/ecommpay/webview`
- `/v1/evaluation/batch`
- `/v1/freeze/apply_offer/`
- `/v1/freeze/can_freeze/`
- `/v1/getrefpromocode`
- `/v1/insurance/`
- `/v1/location/geolocation`
- `/v1/logout/device`
- `/v1/mercadopago/addcard`
- `/v1/mobile/mtsidcheck`
- `/v1/mtspay/addcard`
- `/v1/order/end`
- `/v1/order/make`
- `/v1/order/resume`
- `/v1/order/verify/`
- `/v1/order/wait`
- `/v1/orderinfo/`
- `/v1/orders/aggregation`
- `/v1/parkings/`
- `/v1/paymentinfo/`
- `/v1/pix/verification`
- `/v1/pix/verification/`
- `/v1/places/my`
- `/v1/profile`
- `/v1/profile/aggregated`
- `/v1/profile/avatar`
- `/v1/profile/device`
- `/v1/profile/my/activegoals`
- `/v1/profile/my/goals`
- `/v1/profile/my/promoactions`
- `/v1/profile/my/referralinfo`
- `/v1/profile/warning`
- `/v1/pushwoosh/devices`
- `/v1/unfreeze/`
- `/v1/unsubscribing_reasons`
- `/v1/vehiclefeedback/options`
- `/v1/yookassa/addcard/webview`
- `/v1/yookassa/topup_by_aps`
- `/v2/activity`
- `/v2/bikes/models`
- `/v2/insurance/by_order/`
- `/v2/minutePass/availables`
- `/v2/order/end`
- `/v2/order/photo`
- `/v2/payment/operations`
- `/v2/payment/profile`
- `/v2/places/payment_options`
- `/v2/profile/promocode`
- `/v2/subscriptions/my`
- `/v3/subscriptions/promo_banners`
- `/v3/transports/`
- `/v3/zones/rent`
- `/v3/zones/uses?availableCityTypes=available&availableCityTypes=frozen`
- `/v4/subscriptions/promo_banners`
- `/v5/subscriptions/get_availables`
- `/v5/zones/general`
- `/v6/transports`

## Приватность и ограничения

Не документировались и не коммитились:

- алгоритм или входные данные подписи `ur-request-data`;
- токены, cookie, device IDs, телефоны, email и пользовательские ID;
- сырые request/response body из приложения;
- декомпилированные исходники APK;
- инструкции по обходу клиентских или серверных проверок.
