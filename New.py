import telebot
#import sqlite3
import random

#conn = sqlite3.connect(r'D:\Users\BSarachoglu\Desktop\Tg Bot\tg_bot.db')
#cur = conn.cursor()

bot = telebot.TeleBot('5808660135:AAEi9TipDxdr2u5Vz--06fndV6LwN-Gilt4')

hello = ['Салям', 'Добрый лень', 'Вечер в хату']
text1 = ['Отличный набор', 'Вкусно', 'Рад']
text2 = ['Цена приемлима', 'Гугрик', 'Лучший', 'Прогер']
bye = ['Хорошего дня', 'До свидания!', 'До скорых встреч', 'Пока)']


@bot.message_handler(commands=['start'])
def first(message):
    bot.send_message(message.from_user.id, 'Это бот который что то делает. Напишите сколько текста вы хотите.')
    bot.register_next_step_handler(message, main)


def main(message):
    x = int(message.text)
    for i in range(x):
        no_hello = random.choices(['Да', 'Нет'], [90, 10], k=1)[0]
        no_text1 = random.choices(['Да', 'Нет'], [90, 10], k=1)[0]
        no_text2 = random.choices(['Да', 'Нет'], [90, 10], k=1)[0]
        no_bye = random.choices(['Да', 'Нет'], [90, 10], k=1)[0]
        print(no_hello)
        print(no_text1)
        print(no_text2)
        print(no_bye)
        print('********************************')
        if no_hello == 'Да' and no_text1 == 'Да' and no_text2 == 'Да' and no_bye == 'Да':
            rhello = random.choice(hello) + '. '
            rtext1 = random.choice(text1) + '. '
            rtext2 = random.choice(text2) + '. '
            rbye = random.choice(bye) + '.'
            text = ''
            text += rhello
            text += rtext1
            text += rtext2
            text += rbye
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Да' and no_text1 == 'Да' and no_text2 == 'Да' and no_bye == 'Нет':
            rhello = random.choice(hello) + '. '
            rtext1 = random.choice(text1) + '. '
            rtext2 = random.choice(text2) + '. '
            text = ''
            text += rhello
            text += rtext1
            text += rtext2
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Да' and no_text1 == 'Да' and no_text2 == 'Нет' and no_bye == 'Нет':
            rhello = random.choice(hello) + '. '
            rtext1 = random.choice(text1) + '. '
            text = ''
            text += rhello
            text += rtext1
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Да' and no_text1 == 'Нет' and no_text2 == 'Да' and no_bye == 'Нет':
            rhello = random.choice(hello) + '. '
            rtext2 = random.choice(text1) + '. '
            text = ''
            text += rhello
            text += rtext2
            bot.send_message(message.from_user.id, text)
            bot.send_message(message.from_user.id,
                             'Чтобы воспользоваться этим ботом еще раз просто напишите ту сумму текста которое хотите.')
            bot.register_next_step_handler(message, main)
        elif no_hello == 'Нет' and no_text1 == 'Да' and no_text2 == 'Да' and no_bye == 'Нет':
            rtext1 = random.choice(text1) + '. '
            rtext2 = random.choice(text2) + '. '
            text = ''
            text += rtext1
            text += rtext2
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Нет' and no_text1 == 'Да' and no_text2 == 'Да' and no_bye == 'Да':
            rtext1 = random.choice(text1) + '. '
            rtext2 = random.choice(text2) + '. '
            rbye = random.choice(no_bye) + '.'
            text = ''
            text += rtext1
            text += rtext2
            text += rbye
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Да' and no_text1 == 'Нет' and no_text2 == 'Да' and no_bye == 'Да':
            rhello = random.choice(hello) + '. '
            rtext2 = random.choice(text2) + '. '
            rbye = random.choice(bye) + '.'
            text = ''
            text += rhello
            text += rtext2
            text += rbye
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Да' and no_text1 == 'Да' and no_text2 == 'Нет' and no_bye == 'Да':
            rhello = random.choice(hello) + '. '
            rtext1 = random.choice(text1) + '. '
            rbye = random.choice(bye) + '.'
            text = ''
            text += rhello
            text += rtext1
            text += rbye
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Нет' and no_text1 == 'Да' and no_text2 == 'Нет' and no_bye == 'Нет':
            rtext1 = random.choice(text1) + '. '
            text = ''
            text += rtext1
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Нет' and no_text1 == 'Нет' and no_text2 == 'Да' and no_bye == 'Нет':
            rtext2 = random.choice(text2) + '. '
            text = ''
            text += rtext2
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Нет' and no_text1 == 'Нет' and no_text2 == 'Да' and no_bye == 'Да':
            rtext2 = random.choice(text2) + '. '
            rbye = random.choice(bye) + '.'
            text = ''
            text += rtext2
            text += rbye
            bot.send_message(message.from_user.id, text)
        elif no_hello == 'Нет' and no_text1 == 'Да' and no_text2 == 'Нет' and no_bye == 'Да':
            rtext1 = random.choice(text1) + '. '
            rbye = random.choice(bye) + '.'
            text = ''
            text += rtext1
            text += rbye
            bot.send_message(message.from_user.id, text)
        else:
            rhello = random.choice(hello) + '. '
            rtext1 = random.choice(text1) + '. '
            rtext2 = random.choice(text2) + '. '
            rbye = random.choice(bye) + '.'
            text = ''
            text += rhello
            text += rtext1
            text += rtext2
            text += rbye
            bot.send_message(message.from_user.id, text)
    bot.send_message(message.from_user.id,
                     'Чтобы воспользоваться этим ботом еще раз просто напишите ту сумму текста которое хотите.')
    bot.register_next_step_handler(message, main)


# lst = list()
# name = ''
# surname = ''
# age = 0
# lst = list()
# dictinory = {}
# x = tuple()
#
# cur.execute("""CREATE TABLE IF NOT EXISTS users(
#    id TEXT PRIMARY KEY,
#    name TEXT,
#    surname TEXT,
#    age TEXT);
# """)
# conn.commit()
#
#
# @bot.message_handler(commands=['admin'])
# def first(message):
#     if message.from_user.username != 'MaDn1me':
#         bot.send_message(message.from_user.id,
#                          'У вас нет прав использовать эту команду т.к. вы не являетесь создателем этого бота')
#     else:
#         photo = open(r'D:\Users\BSarachoglu\Desktop\Tg Bot\formuls.jpg', 'rb')
#         bot.send_message(message.from_user.id, 'Здравствуй, Бера!')
#         bot.send_photo(message.from_user.id, photo)
#
#
# @bot.message_handler(commands=['start'])
# def one(message):
#     bot.send_message(message.from_user.id,
#                      'Привет! Я телеграмм бот который получает и обробатывет информацию об пользователе!')
#     bot.send_message(message.from_user.id, 'Для начала спрошу: "Использовал ли ты меня до этого?"')
#     bot.register_next_step_handler(message, yes)
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     global check
#     global user_id
#     check = False
#     user_id = message.from_user.username
#     if message.text == "Привет" or message.text == 'привет':
#         bot.send_message(message.from_user.id,
#                          "Привет! Я телеграмм бот который получает и обробатывет информацию об пользователе!")
#         bot.send_message(message.from_user.id, 'Для начала спрошу: "Использовал ли ты меня до этого?"')
#         bot.register_next_step_handler(message, yes)
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, "Напиши Привет")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
#
#
# def yes(message):
#     if message.text == 'Да':
#         text = ''
#         conn = sqlite3.connect(r'D:\Users\BSarachoglu\Desktop\Tg Bot\tg_bot.db')
#         cur = conn.cursor()
#         user_id = message.from_user.username
#         results = cur.execute("SELECT * FROM users WHERE id = '%s'" % user_id).fetchall()
#         conn.commit()
#         if results == []:
#             bot.send_message(message.from_user.id, 'Вы не зарегестрированы в этом боте.')
#             bot.send_message(message.from_user.id, 'Тогда начнем.')
#             bot.send_message(message.from_user.id, 'Как тебя зовут?')
#             bot.register_next_step_handler(message, second_step)
#         else:
#             idk = results[0]
#             for i in range(len(idk)):
#                 if i > 0:
#                     text += idk[i] + ' '
#             print(results)
#             print(idk)
#             bot.send_message(message.from_user.id, 'Привет, ' + idk[1] + '!')
#     elif message.text == 'Нет':
#         bot.send_message(message.from_user.id, 'Тогда начнем.')
#         bot.send_message(message.from_user.id, 'Как тебя зовут?')
#         bot.register_next_step_handler(message, second_step)
#
#
# def search(message):
#     new = open(r'D:\Users\BSarachoglu\Desktop\Tg Bot\Testofc.txt', 'r', encoding='utf-8')
#     for i in new:
#         lst.append(i.strip())
#     for i in range(len(lst)):
#         print(lst)
#         print(lst[i])
#         if message.text == lst[i]:
#             bot.send_message(message.from_user.id, lst[i + 1])
#
#
# def start(message):
#     bot.send_message(message.from_user.id, 'Как тебя зовут?')
#     bot.register_next_step_handler(message, second_step)
#
#
# def second_step(message):
#     global name
#     name = message.text
#     lst.append(name)
#     bot.send_message(message.from_user.id, 'Хорошо, ' + name + '. Какая у тебя фамилия??')
#     bot.register_next_step_handler(message, third_step)
#
#
# def third_step(message):
#     global surname
#     surname = message.text
#     lst.append(surname)
#     bot.send_message(message.from_user.id, 'Значит твоя фамилия - ' + surname + ', понятно.')
#     bot.send_message(message.from_user.id, 'А сколько тебе лет??')
#     bot.register_next_step_handler(message, last_step)
#
#
# def last_step(message):
#     global age
#     age = message.text
#     lst.append(str(age))
#     keyboard = telebot.types.InlineKeyboardMarkup()
#     key_yes = telebot.types.InlineKeyboardButton(text='Да', callback_data='yes')
#     keyboard.add(key_yes)
#     key_no = telebot.types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(key_no)
#     question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
#     bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     global x
#     if call.data == "yes":
#         bot.send_message(call.message.chat.id, 'Запомню :)')
#         x = (str(user_id), str(name), str(surname), str(age))
#         dictinory[str(user_id)] = surname, name, str(age)
#         print(user_id)
#         print(x)
#         print(type(user_id))
#         conn = sqlite3.connect(r'D:\Users\BSarachoglu\Desktop\Tg Bot\tg_bot.db')
#         cur = conn.cursor()
#         cur.execute("INSERT OR IGNORE INTO users VALUES(?, ?, ?, ?);", x)
#         conn.commit()
#         lst.clear()
#     elif call.data == "no":
#         bot.send_message(call.message.chat.id, 'Значит все по новой -_-')
#         bot.send_message(call.message.chat.id, 'Опять пиши Привет...')


print('Hello world')
bot.polling(none_stop=True, interval=0)
