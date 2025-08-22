# Публикация комиксов XKCD

Этот проект представляет собой Telegram-бота, который получает случайные комиксы XKCD и отправляет их в чат Telegram.

## Установка
1. Скачайте Python версии 3.x

2. Клонируйте репозиторий:

```sh
git clone https://github.com/fiiiiiuuuu/comicsbot.git
cd xkcd-comic-publisher
```

3. Установите необходимые зависимости:

```sh
pip install requirements.txt -r
```

4. Создайте файл `.env` и добавьте в него токен вашего Telegram-бота и id чата:

```
TG_BOT_TOKEN=your_telegram_bot_token
TG_CHAT_ID=your_telegram_chat_id
```

## Использование

Запустите бота, используя следующую команду:

```sh
python telegram_bot.py
```

## Цель проекта

Код написан в образовательных целях в рамках онлайн-курса для веб-разработчиков на [dvmn.org](https://dvmn.org/).
