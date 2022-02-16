
from webbrowser import get
import telebot;
from getEmotion import getEmotion


bot = telebot.TeleBot('5111904045:AAEDPZLqKaacz7BFQV9Aohjj-5gmjEmoUCA');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    strHelp="Привет это интеллектуальный Telegram бот для эмоциального анализа новостей, чем я могу тебе помочь? Для информации введите /help."
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, strHelp)
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Telegram бот для эмоциального анализа новостей. \n Список команд: \n /t - текст для анализа \n ")
    elif splitted_text[0] == "/t":
        str1=""
        for item in splitted_text:
            if item!="/t":
                str1+=" " + item
        bot.send_message(message.from_user.id, getEmotion(str1))    
    else:
        bot.send_message(message.from_user.id, strHelp)

bot.polling(none_stop=True, interval=0)