import telebot
import random

bot = telebot.TeleBot('СЮДА ВВЕДИ СВОЙ ТОКЕН')

hello = ['Салям', 'Добрый лень', 'Вечер в хату']
text1 = ['Отличный набор', 'Вкусно', 'Рад']
text2 = ['Цена приемлима', 'Гугрик', 'Лучший', 'Прогер']
bye = ['Хорошего дня', 'До свидания!', 'До скорых встреч', 'Пока)']

# Приветсвую тебя Рустам
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


bot.polling(none_stop=True, interval=0)
