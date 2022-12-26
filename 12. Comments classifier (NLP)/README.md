# Определение токсичных комментариев

**Иcходные данные**

Интернет-магазин запускает новый сервис. Теперь пользователи могут редактировать и дополнять описания товаров, как в вики-сообществах. То есть клиенты предлагают свои правки и комментируют изменения других.

В нашем распоряжении набор данных с разметкой о токсичности правок.

**Цель исследования**

Магазину нужен инструмент, который будет искать токсичные комментарии и отправлять их на модерацию.

Необходимо создать модель для классифицикации комментариев на позитивные и негативные.

Метрика качества *F1* на тестовой выборке должно быть не меньше 0.75.


**Ход исследования**

1. Обзор и подготовка данных.
2. Обучение и проверка различных моделей.
3. Финальное тестирование лучшей модели.
4. Вывод.