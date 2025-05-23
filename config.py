import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot settings
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Topics
TOPICS = {
    "ВУЗ": "questions/vuz.txt",
    "Медицина": "questions/medicine.txt",
    "Общежитие": "questions/dormitory.txt",
    "Военкомат": "questions/military.txt"
}

# Emojis
EMOJIS = {
    "question": "❓",
    "answer": "📝",
    "back": "◀️",
    "search": "🔍",
    "help": "❔",
    "info": "ℹ️"
}

# Messages
MESSAGES = {
    "welcome": "Добро пожаловать! Я бот-помощник МГТУ. Выберите интересующую вас тему:",
    "select_topic": "Выберите интересующую вас тему:",
    "select_question": "Выберите интересующий вас вопрос по теме {}:",
    "search_placeholder": "Введите ключевые слова для поиска...",
    "no_results": "По вашему запросу ничего не найдено. Попробуйте изменить поисковый запрос.",
    "help": """Я бот-помощник МГТУ. Вот что я умею:

1. Отвечать на вопросы по темам:
   - ВУЗ (стипендии, учеба)
   - Медицина (поликлиника, медосмотры)
   - Общежитие (проживание, правила)
   - Военкомат (отсрочки, призыв)

2. Искать информацию по ключевым словам
3. Показывать справку по команде /help

Для начала работы выберите интересующую вас тему или используйте поиск.""",
    "error": "Произошла ошибка. Пожалуйста, попробуйте позже."
} 