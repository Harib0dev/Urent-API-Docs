# Наблюдения Loon-сессии 2025-09-22

Источник: локальный экспорт Loon `1838_1758554286292.zip`.

Сырые запросы, заголовки и тела не добавлены в репозиторий. Из экспорта использованы только обезличенные признаки: host, HTTP method, путь, статус, имена query-параметров и форма JSON (`ключ -> тип`).

## Сводка

- Всего request header-файлов: 397
- запросов, связанных с Urent: 243
- уникальных Urent-операций после нормализации: 53
- покрытие после обновления `openapi.yaml`: 67 операций в спецификации

## Основные host

- `app.urentbike.ru`
- `lg.service.urentbike.ru`
- `notification.service.urentbike.ru`
- `backyard.urentbike.ru`

## Что добавлено в спецификацию

- авторизация: `POST /v1/connect/token`
- устройства: `POST /v1/devices/my/token`
- аренда: `POST /v1/order/wait`, `POST /v1/order/resume`, `POST /v2/order/end`
- проверка и тарифы: `GET /v1/order/verify/S.{scooter_id}`, `GET /v1/profile/rate/S.{scooter_id}`
- заказ: `GET /v1/orderinfo/{order_id}/info`
- профиль: `GET /v1/profile/aggregated`, `GET /v1/profile/my/goals`, `GET /v1/profile/warning`
- feedback: `GET /v1/vehiclefeedback/options`
- подписки и пакеты: `GET /v1/customerAbonements/my`, `GET /v2/minutePass/availables`, `GET /v2/subscriptions/my`, `GET /v5/subscriptions/get_availables`, `GET /v3/subscriptions/promo_banners`, `GET /v4/subscriptions/promo_banners`
- повербанки: `GET /powerbank/v1/nearest`
- файлы: `GET /file/{date}/{file_name}`
- feature flags: `POST /flagr/api/v1/evaluation/batch`
- телеметрия: `POST /` на `lg.service.urentbike.ru`

## Приватность

При обработке экспорта не коммитились:

- `Authorization`, JWT, refresh tokens, cookies;
- `ur-request-data`;
- device tokens и device IDs;
- телефоны, user IDs, session IDs;
- точные значения координат из запросов.
