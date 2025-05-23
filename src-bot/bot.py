import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from config import BOT_TOKEN, MESSAGES
from handlers import (
    cmd_start, cmd_help, handle_topic, handle_search,
    process_search, process_question, back_to_questions, back_to_main, back_to_search
)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Register handlers
dp.message.register(cmd_start, Command("start"))
dp.message.register(cmd_help, Command("help"))
dp.message.register(handle_topic, lambda message: message.text in ["ВУЗ", "Медицина", "Общежитие", "Военкомат"])
dp.message.register(handle_search, lambda message: message.text == "🔍 Поиск")
dp.message.register(process_search, lambda message: message.text != "🔍 Поиск" and message.text != "❔ Помощь")
dp.callback_query.register(process_question, lambda c: c.data.startswith('q_'))
dp.callback_query.register(back_to_questions, lambda c: c.data.startswith('back_to_') and c.data != "back_to_main" and c.data != "back_to_search")
dp.callback_query.register(back_to_main, lambda c: c.data == "back_to_main")
dp.callback_query.register(back_to_search, lambda c: c.data == "back_to_search")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 