import telebot
import sqlite3
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

users ={}
user_name={}
user_surname={}
phone_number={}
procedure_type={}
procedure_date={}
procedure_time={}

# conn = sqlite3.connect('database.db', check_same_thread=False)
# cursor = conn.cursor()
# def db_table_val(user_id: int,
#                  name: str,
#                  surname: str,
#                  phone_number: str,
#                  procedure_type: str,
#                  procedure_date: str,
#                  procedure_time: str):
# 	cursor.execute('INSERT INTO test (user_id, '
#                    'user_name, '
#                    'user_surname, '
#                    'username,'
#                    'phone_number,'
#                    'procedure_date,'
#                    'procedure_time) VALUES (?, ?, ?, ?)', (user_id,
#                                                            name,
#                                                            surname,
#                                                            phone_number,
#                                                            procedure_type,
#                                                            procedure_date,
#                                                            procedure_time
#                                                            ))
# 	conn.commit()
#
#
#
# # добавили кнопки
# @bot.message_handler(commands=['help', 'start'])
# def menu(message: telebot.types.Message):
#     chat_id = message.chat.id
#     keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button_order = telebot.types.KeyboardButton(text="Записаться")
#     # button1 = telebot.types.KeyboardButton(text="Массаж спины")
#     # button2 = telebot.types.KeyboardButton(text="Массаж ног")
#     # button3 = telebot.types.KeyboardButton(text="Массаж рук")
#     keyboard.add(button_order)
#     bot.send_message(chat_id,
#                      'Добро пожаловать в бота сбора обратной связи',
#                      reply_markup=keyboard)
#
#
#
# @bot.message_handler(
#     func=lambda message: message.text == 'Записаться')
# def order(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, 'Введите своё имя')
#     users[chat_id] = {}
#     bot.register_next_step_handler(message, save_username)
#
# # сохраняем имя
# def save_username(message):
#     chat_id = message.chat.id
#     name = message.text
#     users[chat_id]['name'] = name
#     bot.send_message(chat_id, f'Отлично. Теперь укажи свою фамилию')
#     bot.register_next_step_handler(message, save_surname)
#
# # сохраняем и фамилию
# def save_surname(message):
#     chat_id = message.chat.id
#     surname = message.text
#     users[chat_id]['surname'] = surname
#     bot.send_message(chat_id, f'Отлично. Теперь укажи свой номер телефона')
#     bot.register_next_step_handler(message, save_phone_number)
#
#
# # сохраняем  номер телефона
# def save_phone_number(message):
#     chat_id = message.chat.id
#     phone_number = message.text
#     users[chat_id]['phone_number'] = phone_number
#     bot.send_message(chat_id, f'Отлично. Теперь укажи вид процедуры')
#     bot.register_next_step_handler(message, procedure_type)
#
# def procedure_type(message):
#     chat_id = message.chat.id
#     procedure_type = message.text
#     users[chat_id]['procedure_type'] = procedure_type
#     bot.send_message(chat_id, f'Отлично. Теперь укажи дату процедуры')
#     bot.register_next_step_handler(message, procedure_date)
#
# def procedure_date(message):
#     chat_id = message.chat.id
#     procedure_date = message.text
#     users[chat_id]['procedure_date'] = procedure_date
#     bot.send_message(chat_id, f'Отлично. Теперь укажи время процедуры')
#     bot.register_next_step_handler(message, procedure_time)
#
# def procedure_time(message):
#     chat_id = message.chat.id
#     procedure_time = message.text
#     users[chat_id]['procedure_time'] = procedure_time
#     name = users[chat_id]['name']
#     surname = users[chat_id]['surname']
#     phone_number = users[chat_id]['phone_number']
#     procedure_type = users[chat_id]['procedure_type']
#     procedure_date = users[chat_id]['procedure_date']
#     text = f'Ваше имя {name} Ваша фамилия {surname} Ваш номер {phone_number} Процедура {procedure_type} Дата {procedure_date} Время {procedure_time}'
#     bot.send_message(message.chat.id, text)
#
#     us_id = message.from_user.id
#     name = message.text
#     surname = message.text
#     phone_number = message.text
#     procedure_type = message.text
#     procedure_date = message.text
#     procedure_time = message.text
#
#
#     db_table_val(user_id=us_id,
#                  user_name=name,
#                  user_surname=surname,
#                  phone_number=phone_number,
#                  procedure_type=procedure_type,
#                  procedure_date=procedure_date,
#                  procedure_time=procedure_time,
#                  )

name = ''


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('db.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary_key, name varchar(50), phone_num name varchar(11))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'регистрация данных, введите имя')
    bot.register_next_step_handler(message, us_name)


def us_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, "Ваше телефон" )
    bot.register_next_step_handler(message, us_phone)

def us_phone(message):
    phone_num = message.text

    conn = sqlite3.connect('db.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, phone_num) VALUES ('%s', '%s')" % (name, phone_num))
    conn.commit()
    cur.close()
    conn.close()


    bot.send_message(message.chat.id, 'Готово')




    # bot.send_message(message.chat.id, "Ваше телефон" )
    # bot.register_next_step_handler(message, us_phone)






bot.polling(none_stop=True)