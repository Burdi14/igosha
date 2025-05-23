from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOPICS, EMOJIS

def load_questions_from_file(filename):
    questions = {}
    current_question = None
    current_answer = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
                
            if line[0].isdigit() and '. ' in line:
                if current_question:
                    questions[current_question] = '\n'.join(current_answer)
                current_question = line.split('. ', 1)[1]  # Убираем номер вопроса
                current_answer = []
            else:
                current_answer.append(line)
                
    if current_question:
        questions[current_question] = '\n'.join(current_answer)
    
    return questions

def get_main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="ВУЗ")],
            [KeyboardButton(text="Медицина")],
            [KeyboardButton(text="Общежитие")],
            [KeyboardButton(text="Военкомат")],
            [KeyboardButton(text=f"{EMOJIS['search']} Поиск")]
        ],
        resize_keyboard=True
    )
    return keyboard

def get_questions_keyboard(topic):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=question, callback_data=f"q_{topic}_{i}")]
            for i, question in enumerate(QUESTIONS[topic].keys(), 1)
        ] + [[InlineKeyboardButton(text=f"{EMOJIS['back']} Назад", callback_data="back_to_main")]]
    )
    return keyboard

def get_back_keyboard(topic):
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f"{EMOJIS['back']} Назад к вопросам", callback_data=f"back_to_{topic}")]]
    )

def search_questions(query):
    if len(query) < 3:
        return []
        
    results = []
    query = query.lower()
    
    for topic, filename in TOPICS.items():
        questions = load_questions_from_file(filename)
        for i, (question, answer) in enumerate(questions.items(), 1):
            if query in question.lower() or query in answer.lower():
                # Сортируем результаты: сначала совпадения в вопросе, потом в ответе
                priority = 0
                if query in question.lower():
                    priority = 1
                results.append({
                    'topic': topic,
                    'num': str(i),
                    'question': question,
                    'answer': answer,
                    'priority': priority
                })
    
    # Сортируем результаты по приоритету (сначала совпадения в вопросе)
    results.sort(key=lambda x: (-x['priority'], x['question']))
    return results

# Load all questions
QUESTIONS = {topic: load_questions_from_file(filename) for topic, filename in TOPICS.items()} 