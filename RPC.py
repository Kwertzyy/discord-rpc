############################### #- Stormwares.xyz is Owned by Kwertzyy#7139
############################### #- Owned by Kwertzyy#7139 ©️ to Stormwares.xyz

import discord
import win32console as wc
from pypresence import Presence
from pystyle import *
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import time
import os

############################### #- Owned by Kwertzyy#7139 ©️ to Stormwares.xyz

vítej = """
 ___  ____  _____  ____  __  __    ____  ____   ___ 
/ __)(_  _)(  _  )(  _ \(  \/  )  (  _ \(  _ \ / __)
\__ \  )(   )(_)(  )   / )    (    )   / )___/( (__ 
(___/ (__) (_____)(_)\_)(_/\/\_)  (_)\_)(__)   \___)
"""

while True:
    Write.Print(f"{vítej}", Colors.blue_to_cyan, interval=0.000)
    Write.Print("               Made by Kwertzyy#7139", Colors.light_gray, interval=0.030)
    print("")
    print("")
    id = Write.Input("[>>] Application ID: ", Colors.blue_to_cyan, interval=0.030)
    RPC = Presence(id)
    RPC.connect()
    state = Write.Input("[>>] State of presence: ", Colors.blue_to_cyan, interval=0.030)
    details = Write.Input("[>>] Details of presence: ", Colors.blue_to_cyan, interval=0.030)
    large_image = Write.Input("[>>] Large Image of presence: ", Colors.blue_to_cyan, interval=0.030)
    large_text = Write.Input("[>>] Text in large text of presence: ", Colors.blue_to_cyan, interval=0.030)
    start_time=time.time()
    RPC.update(state=f"{state}", details=f"{details}", large_image=f"{large_image}", large_text=f"{large_text}", start=start_time, buttons = [{"label": "Using Stormwares.xyz RPC tool!", "url": "https://stormwares.xyz"}])
    Write.Print("!!! Keep me open for working on discord !!!", Colors.red_to_yellow, interval=0.030)
    os.system("cls")
    Write.Print("!!! Keep me open for working on discord !!!", Colors.red_to_yellow, interval=0.030)
    os.system("cls")
    Write.Print("!!! Keep me open for working on discord !!!", Colors.red_to_yellow, interval=0.030)
    os.system("cls")
    Write.Print("!!! Keep me open for working on discord !!!", Colors.red_to_yellow, interval=0.030)
    os.system("cls")
    Write.Input("!!! Keep me open for working on discord !!!", Colors.red_to_yellow, interval=0.030)