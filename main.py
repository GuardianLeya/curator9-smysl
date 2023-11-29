import telebot
bot = telebot.TeleBot("6510093481:AAEwrx-n3shTpBPduQzEgdxQLBKY7b7FQRo")
@bot.message_handler(commands=["Start"])
def main(message):
    bot.send_message(message.chat.id,"Привет,Чем могу помочь ?")
@bot.message_handler(commands=["link"])
def main(message):
    bot.send_message(message.chat.id,"Ссылка:https://www.youtube.com/watch?v=fp5-XQFr_nk")
@bot.message_handler(commands=["information"])
def main(message):
    bot.send_message(message.chat.id,"Python - это популярный язык программирования, который позволяет работать быстро и интегрировать системы более эффективно.  \nPython может использоваться на сервере для создания веб-приложений. \nПоследняя версия Python на момент написания этого сообщения - Python 3.12.03. \nВы можете загрузить Python и установить его на своем компьютер \nЕсли вы новичок в программировании или опытный разработчик, Python легко изучить и использовать.  \nВы можете начать с руководства для начинающих на официальном сайте Python")
bot.infinity_polling()