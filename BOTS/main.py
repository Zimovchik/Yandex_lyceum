import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import time

TOKEN = "5267078948:AAFG-FedHnO1ABqgm8byjHDUcwN0cR3DaAk"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def echo(update, context):
    update.message.reply_text("Я получил сообщение " + update.message.text)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text & ~Filters.command, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("dice", dice))
    updater.idle()


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


k1 = ReplyKeyboardMarkup([["/dice", "/timer"]], one_time_keyboard=False)
k2 = ReplyKeyboardMarkup([["кинуть один шестигранный кубик"],
                          ["кинуть 2 шестигранных кубика одновременно"],
                          ["кинуть 20-гранный кубик"],
                          ["вернуться назад"]])


def start(update, context):
    update.message.reply_text("Я бот для настольных игр", reply_markup=k1)


def help(update, context):
    update.message.reply_text("Я беспомощен. Как, впрочем, и ты.")


def dice(update, context):
    # update.message.reply_text(reply_markup=)
    update.message.reply_text("Какой кубик бросить?", reply_markup=k2)
    pass


if __name__ == '__main__':
    main()
