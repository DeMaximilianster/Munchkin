from presenter.config.token import bot
from telebot import logger


@bot.message_handler(commands=['start', 'help'])
def answer(message):
    bot.reply_to(message, "Если вы это читаете, для вас хорошие новости. Гениальный @DeMaximilianster и его... партнёры? сотрудники? товарищи? помощники? @ProBeUs и @artm04 разрабатывают бота для игры в великолепную игру 'Манчкин' прямо в Телеграме!")


@bot.message_handler(commands=['test', 'test_pic'])
def test(message):
    bot.send_photo(message.chat.id, "AgADAgADrqsxG0Le0UgY3xAe2q1FZ7vrug8ABAEAAwIAA20AA5lRAwABFgQ")


logger.setLevel("DEBUG")
bot.polling()
