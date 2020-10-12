import telebot
while True:
    try:
        bot = telebot.TeleBot('1259786699:AAH0F8jicygEYUAXabb0MeO3YY78vS9v9lc')

        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id, 'Привет, посмотри на описание бота и напиши любое сообшение)))')

        @bot.message_handler(commands=['starting'])
        def starting_message(message):
            bot.send_message(1372812835, 'ого, маэш класный хуй')

        @bot.message_handler(content_types=['text'])
        def send_message(message):
            bot.send_message(message.chat.id, 'Ты королева вселенной 💕')
            bot.send_message(704752422, message.text)

        bot.polling()
    except:
        pass
        
