from aiogram import types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MESSAGES, EMOJIS
from utils import get_main_menu_keyboard, get_questions_keyboard, get_back_keyboard, QUESTIONS, search_questions

async def cmd_start(message: types.Message):
    await message.answer(MESSAGES["welcome"], reply_markup=get_main_menu_keyboard())

async def cmd_help(message: types.Message):
    await message.answer(MESSAGES["help"])

async def handle_topic(message: types.Message):
    topic = message.text
    await message.answer(
        MESSAGES["select_question"].format(topic),
        reply_markup=get_questions_keyboard(topic)
    )

async def handle_search(message: types.Message):
    await message.answer(MESSAGES["search_placeholder"])

async def process_search(message: types.Message):
    query = message.text.strip()
    if len(query) < 3:
        await message.answer("Поисковый запрос должен содержать минимум 3 символа.")
        return

    results = search_questions(query)
    if not results:
        await message.answer(MESSAGES["no_results"])
        return

    response = f"🔍 Результаты поиска по запросу: *{query}*\n\n"
    for i, result in enumerate(results[:5], 1):
        response += f"*{i}. {result['question']}*\n"
        response += f"{result['answer']}\n\n"

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f"{EMOJIS['back']} Назад к вопросам", callback_data="back_to_search")]]
    )

    await message.answer(
        response,
        parse_mode="Markdown",
        reply_markup=keyboard
    )
async def process_question(callback_query: types.CallbackQuery):
    _, topic, num = callback_query.data.split('_')
    question = list(QUESTIONS[topic].keys())[int(num) - 1]
    answer = QUESTIONS[topic][question]

    is_photo_question = topic.lower() == "медицина" and num == '3'

    if is_photo_question:
        # Always delete and send a new photo message
        try:
            await callback_query.message.delete()
        except Exception:
            pass  # Message might already be gone or not deletable

        await callback_query.message.answer_document(
            document=types.FSInputFile("files/schedule_doctors.pdf"),
            caption=f"*{question}*\n\n{EMOJIS['answer']} Ответ:\n{answer}",
            parse_mode="Markdown",
            reply_markup=get_back_keyboard(topic)
        )
    else:
        await callback_query.message.edit_text(
            f"*{question}*\n\n{EMOJIS['answer']} Ответ:\n{answer}",
            reply_markup=get_back_keyboard(topic),
            parse_mode="Markdown"
        )
    await callback_query.answer()

async def back_to_questions(callback_query: types.CallbackQuery):
    topic = callback_query.data.split('_')[2]
    is_photo_question = topic.lower() == "медицина" and callback_query.message.document is not None

    if is_photo_question:
        try:
            await callback_query.message.delete()
        except Exception:
            pass

        await callback_query.message.answer(
            MESSAGES["select_question"].format(topic),
            reply_markup=get_questions_keyboard(topic)
        )
    else:
        await callback_query.message.edit_text(
            MESSAGES["select_question"].format(topic),
            reply_markup=get_questions_keyboard(topic)
        )

    await callback_query.answer()

async def back_to_main(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer(
        MESSAGES['select_topic'],
        reply_markup=get_main_menu_keyboard()
    )
    await callback_query.answer()

async def back_to_search(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer(
        MESSAGES["search_placeholder"]
    )
    await callback_query.answer() 