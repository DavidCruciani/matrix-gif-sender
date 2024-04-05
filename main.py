"""
Example Usage:

random_user
      !gif excited
"""

import simplematrixbotlib as botlib
import config as Config
import requests
import random
import json

config = botlib.Config()
config.encryption_enabled = True  # Automatically enabled by installing encryption support
config.ignore_unverified_devices = True

creds = botlib.Creds(Config.MATRIX_SERVER, Config.MATRIX_USER, Config.MATRIX_PASSWORD, device_name=Config.MATRIX_DEVICE_NAME)
bot = botlib.Bot(creds, config)
PREFIX = '!'

image_filepath = "gif_sender.gif"
limit=200

def get_gif(searchTerm):
    if Config.TENOR_API_KEY == "LIVDSRZULELA":
        response = requests.get(f"https://g.tenor.com/v1/random?q={searchTerm}&key={Config.TENOR_API_KEY}&limit=1")
        data = response.json()
        
        if data["results"]:
            uri = data['results'][0]['media'][0]['gif']['url']
        else:
            return False
    else:
        response = requests.get(f"https://tenor.googleapis.com/v2/search?q={searchTerm}&key={Config.TENOR_API_KEY}&client_key={Config.TENOR_CLIENT_KEY}&limit={limit}")
        data = json.loads(response.content)
        
        # see urls for all GIFs
        if data["results"]:
            gif = random.choice(data['results'])
            uri = gif["media_formats"]["gif"]["url"]
        else:
            return False
        
    with open(image_filepath, "wb") as f:
        f.write(requests.get(uri).content)
    return True
    

@bot.listener.on_message_event
async def gif_sender(room, message):
    global last_command
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.prefix():
        if match.command("gif"):
            if get_gif(" ".join(arg for arg in match.args())):
                await bot.api.send_image_message(room.room_id, image_filepath)
            else:
                await bot.api.send_text_message(room.room_id, "Gif not found... Sorry", reply_to=message.event_id)

bot.run()
