import telebot
from telebot import types

TOKEN = 'You token'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('General social networks.')
    button2 = types.KeyboardButton('Microblogs.')
    button3 = types.KeyboardButton('Social networks for sharing photos and videos.')
    button4 = types.KeyboardButton('Video platforms.')
    button5 = types.KeyboardButton('Messengers with social network functions.')
    button6 = types.KeyboardButton('Forums and communities')
    button7 = types.KeyboardButton('Gaming social networks')

    markup.add(button1, button2, button3)
    markup.add(button4, button5, button6, button7)

    bot.send_message(
        message.chat.id,
        'Hellow {0.first_name}.'.format(message.from_user),
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    if message.text == 'General social networks.':
        markup = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Facebook', url='https://www.facebook.com')

        markup.add(but1)

        bot.send_message(
            message.chat.id,
            'These platforms are designed for a wide range of users and provide a variety of opportunities for communication, publication and content sharing:',
            reply_markup=markup
        )

    if message.text == 'Microblogs.':
        markup = types.InlineKeyboardMarkup()
        but2 = types.InlineKeyboardButton('Twitter', url='https://x.com/')

        markup.add(but2)

        bot.send_message(
            message.chat.id,
            'A format for short posts or updates that users can quickly read and share:',
            reply_markup=markup
        )

    if message.text == 'Social networks for sharing photos and videos.':
        markup = types.InlineKeyboardMarkup()
        but3 = types.InlineKeyboardButton('Pinterest', url='https://www.pinterest.com/')
        but4 = types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/')

        markup.add(but3, but4)

        bot.send_message(
            message.chat.id,
            'Designed for creating, publishing and sharing visual content:',
            reply_markup=markup
        )

    if message.text == 'Video platforms.':
        markup = types.InlineKeyboardMarkup()
        but5 = types.InlineKeyboardButton('Youtube', url='https://www.youtube.com/')
        but6 = types.InlineKeyboardButton('Tiktok', url='https://www.tiktok.com/')

        markup.add(but5, but6)

        bot.send_message(
            message.chat.id,
            'They focus on creating and viewing video content:',
            reply_markup=markup
        )

    if message.text == 'Messengers with social network functions.':
        markup = types.InlineKeyboardMarkup()
        but7 = types.InlineKeyboardButton('Whatsapp', url='https://www.whatsapp.com/')

        markup.add(but7)

        bot.send_message(
            message.chat.id,
            "Today's messengers often include social networking elements such as channels, groups, and news feeds:",
            reply_markup=markup
        )

    if message.text == 'Forums and communities':
        markup = types.InlineKeyboardMarkup()
        but8 = types.InlineKeyboardButton('Reddit', url='https://www.reddit.com/')

        markup.add(but8)

        bot.send_message(
            message.chat.id,
            "They focus on discussing certain topics in the form of posts and comments:",
            reply_markup=markup
        )

    if message.text == 'Gaming social networks':
        markup = types.InlineKeyboardMarkup()
        but9 = types.InlineKeyboardButton('Twitch', url='https://www.twitch.tv/')
        but10 = types.InlineKeyboardButton('Discord', url='https://discord.com/')

        markup.add(but9, but10)

        bot.send_message(
            message.chat.id,
            "Focused on gamers, where you can communicate, share game achievements and meet like-minded people:",
            reply_markup=markup
        )

bot.polling(non_stop=True)
