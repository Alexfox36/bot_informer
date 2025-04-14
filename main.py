import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
users ={}



# добавили кнопки
@bot.message_handler(commands=['help', 'start'])
def menu(message: telebot.types.Message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_order = telebot.types.KeyboardButton(text="Записаться")
    button1 = telebot.types.KeyboardButton(text="Массаж спины")
    button2 = telebot.types.KeyboardButton(text="Массаж ног")
    button3 = telebot.types.KeyboardButton(text="Массаж рук")
    keyboard.add(button_order, button1, button2, button3)
    bot.send_message(chat_id,
                     'Добро пожаловать в бота сбора обратной связи',
                     reply_markup=keyboard)



@bot.message_handler(
    func=lambda message: message.text == 'Записаться')
def order(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Введите своё имя')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)

# сохраняем имя
def save_username(message):
    chat_id = message.chat.id
    name = message.text
    users[chat_id]['name'] = name
    bot.send_message(chat_id, f'Отлично. Теперь укажи свою фамилию')
    bot.register_next_step_handler(message, save_surname)

# сохраняем и фамилию
def save_surname(message):
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname
    bot.send_message(chat_id, f'Отлично. Теперь укажи свой номер телефона')
    bot.register_next_step_handler(message, save_phone_number)


# сохраняем  номер телефона
def save_phone_number(message):
    chat_id = message.chat.id
    phone_number = message.text
    users[chat_id]['phone_number'] = phone_number
    bot.send_message(chat_id, f'Отлично. Теперь укажи вид процедуры')
    bot.register_next_step_handler(message, procedure_type)

def procedure_type(message):
    chat_id = message.chat.id
    procedure_type = message.text
    users[chat_id]['procedure_type'] = procedure_type
    bot.send_message(chat_id, f'Отлично. Теперь укажи дату процедуры')
    bot.register_next_step_handler(message, procedure_date)

def procedure_date(message):
    chat_id = message.chat.id
    procedure_date = message.text
    users[chat_id]['procedure_date'] = procedure_date
    bot.send_message(chat_id, f'Отлично. Теперь укажи время процедуры')
    bot.register_next_step_handler(message, procedure_time)

def procedure_time(message):
    chat_id = message.chat.id
    procedure_time = message.text
    users[chat_id]['procedure_time'] = procedure_time
    name = users[chat_id]['name']
    surname = users[chat_id]['surname']
    phone_number = users[chat_id]['phone_number']
    procedure_type = users[chat_id]['procedure_type']
    procedure_date = users[chat_id]['procedure_date']
    text = f'Ваше имя {name} Ваша фамилия {surname} Ваш номер {phone_number} Процедура {procedure_type} Дата {procedure_date} Время {procedure_time}'
    bot.send_message(message.chat.id, text)







bot.polling(none_stop=True)