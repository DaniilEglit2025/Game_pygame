import telebot

token = '7926374435:AAEZv4NAnFAcI_Qmv_I0S8f9caLk-ACAc1M'

bot = telebot.TeleBot(token)

help = '''Мой бот умеет
/todo команда для добавления '''

@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()
