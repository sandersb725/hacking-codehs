import os

os.system("pip install hugchat && clear")

import base64
from hugchat import hugchat
from hugchat.login import Login

EMAIL = "bus120610@gmail.com"
PASSWD = base64.b64decode("TiZZUHIza1dyKDZkVlNt".encode("ascii")).decode("ascii")
cookie_path_dir = "./cookies/"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

print(chatbot.chat("Hi!"))

while True:
     print(chatbot.chat(input("> ")))
