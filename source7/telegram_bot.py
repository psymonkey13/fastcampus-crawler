import telegram

bot = telegram.Bot(token='562773657:AAGxPrC-d42HH_onCWrJRJ9MTnpjVwdHLN4')
# chat_id = bot.getUpdates()[-1].message.chat.id
bot.sendMessage(chat_id=570871023, text='안녕하세요.')