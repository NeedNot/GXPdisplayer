import requests

g = requests.get('https://api.hypixel.net/guild?key=APIKEY&name=GUILD NAME').json()



for i in range(len(g['guild']['members'])):
  uuid = g['guild']['members'][i]['uuid']

  x = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
  x = x.json()

  expHistory = g['guild']['members'][i]['expHistory']
  print(f"{x['name']} Last 7 Days Guild XP {sum(expHistory.values())}\n")
