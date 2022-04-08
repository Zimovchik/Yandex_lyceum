import os
import sys
import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests


def get_coords(place):
    a = place
    geocoder_request = \
        "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" + a + "&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        name = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        return name["boundedBy"]["Envelope"]["lowerCorner"], name["boundedBy"]["Envelope"]["upperCorner"], \
               name["Point"]["pos"]

    else:
        print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")


def get_image(lc, uc, name):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&?l=map&bbox={lc}~{uc}"
    response = requests.get(geocoder_request)
    if response:
        return response
    else:
        print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")


TOKEN = "5267078948:AAFG-FedHnO1ABqgm8byjHDUcwN0cR3DaAk"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text & ~Filters.command, message_respond)
    dp.add_handler(text_handler)
    updater.start_polling()
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("map", location_map))
    # dp.add_handler(CommandHandler("restart", restart))
    # dp.add_handler(CommandHandler("stop", stop))
    updater.idle()


def message_respond(update, context):
    pass


def start(update, context):
    update.message.reply_text("Hello, i'm geobot. Use /map <place> to get the map of some place.")


def location_map(update, context):
    coords = get_coords(update.message.text)
    print(coords)
    id = update.message.chat_id
    context.bot.send_photo(id, get_image(*coords))


# update.message.reply_text("")

def help(update, context):
    update.message.reply_text("I'm unable to help you for now.")


if __name__ == '__main__':
    main()
