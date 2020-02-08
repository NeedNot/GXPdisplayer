import requests
import os
from api_key import api_key


guild = input("ENTER A GUILD NAME:")

gurl = ("https://api.hypixel.net/guild?key=" + api_key + "&name=" + guild)
g = requests.get(gurl)
g = g.json()

print('------------------------------------------')
for i in range(len(g['guild']['members'])):
  uuid = g['guild']['members'][i]['uuid']

  x = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
  x = x.json()

  expHistory = g['guild']['members'][i]['expHistory']
  print(f"{x['name']} Last 7 Days Guild XP {sum(expHistory.values())}\n")

os.system("pause")
