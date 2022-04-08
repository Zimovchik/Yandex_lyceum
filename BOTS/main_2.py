import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import time

TOKEN = "5267078948:AAFG-FedHnO1ABqgm8byjHDUcwN0cR3DaAk"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

# def echo(update, context):
#     update.message.reply_text("Я получил сообщение " + update.message.text)


poem = """Ты богат, я очень беден;
Ты прозаик, я поэт;
Ты румян, как маков цвет,
Я, как смерть, и тощ и бледен.
Не имея ввек забот,
Ты живешь в огромном доме;
Я ж средь горя и хлопот
Провожу дни на соломе.""".split('\n')
current_index = 0
workable = False


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text & ~Filters.command, line_check)
    dp.add_handler(text_handler)
    updater.start_polling()
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("suphler", suphler))
    dp.add_handler(CommandHandler("restart", restart))
    dp.add_handler(CommandHandler("stop", stop))
    updater.idle()


def start(update, context):
    global workable
    global current_index
    update.message.reply_text(poem[0])
    current_index += 1
    workable = True


def line_check(update, context):
    global workable
    if workable:
        global current_index
        print(update.message.text, poem[current_index])
        if update.message.text == poem[current_index]:
            current_index += 3
            try:
                update.message.reply_text(poem[current_index - 1])
            except IndexError:
                update.message.reply_text(
                    "Стихотворение закончилось. Начнем заново?(чтобы начать заново введите команду /restart)")
                workable = False
        elif current_index in range(0, len(poem)):
            suphler(update, context)
        else:
            update.message.reply_text(
                "Стихотворение закончилось. Начнем заново?(чтобы начать заново введите команду /restart)")


def help(update, context):
    update.message.reply_text("Я беспомощен. Как, впрочем, и ты.")


def suphler(update, context):
    update.message.reply_text("Правильная строка: " + poem[current_index])


def restart(update, context):
    global workable
    global current_index
    print('a')
    current_index = 0
    update.message.reply_text(poem[0])
    current_index += 1
    workable = True


def stop(update, context):
    update.message.reply_text("Работа бота приостановлена, если хотите продолжить введите:\n/start or\n/restart")
    global workable
    workable = False


if __name__ == '__main__':
    main()
