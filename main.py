import telebot
from telebot import types


bot = telebot.TeleBot('5480049603:AAHyx4ZjEKNQmVVDJJiHVK4qg3KhNHBqVwg')


@bot.message_handler(commands=['start'])  # Срабатывание на комаду
def start(message):
    mess = f'Здарова, <b>{message.from_user.first_name}</b> чего хотел?'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['vk']) # создание кнопки и реагирование
def vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить вк создателя", url="https://vk.com/danilsocol"))
    bot.send_message(message.chat.id, "Вот вам мой батёк", reply_markup=markup)


@bot.message_handler(commands=['help'])  # создание меню при команде
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    web = types.KeyboardButton('/vk')
    start = types.KeyboardButton('/start')
    markup.add(web,start)
    bot.send_message(message.chat.id, "Ну раз ты просишь", reply_markup=markup)



@bot.message_handler(content_types=['photo'])  # срабатывает на тот или иной тип сообщения
def dey_user_photo(message):
    bot.send_message(message.chat.id, "Крутое фото, спору нет", parse_mode='html')


@bot.message_handler()  # Всегда срабатывает на любое действие
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Нахер ты с ботом здороваешься?", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "logo":
        photo = open('icons/logo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, f"Я тебя не понимаю", parse_mode='html')


bot.polling(none_stop=True)
