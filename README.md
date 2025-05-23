# МГТУ Helper Bot

Telegram бот-помощник для студентов МГТУ, предоставляющий информацию по различным темам:
- ВУЗ
- Медицина
- Общежитие
- Военкомат

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` и добавьте в него токен вашего бота:
```bash
cp .env.example .env
```
Отредактируйте файл `.env` и замените `your_bot_token_here` на ваш токен от @BotFather.

## Запуск

```bash
python bot.py
```