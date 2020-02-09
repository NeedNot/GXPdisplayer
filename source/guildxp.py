import requests
import time

try:
    with open('API_KEY') as inf:
        api_key = inf.read()
except FileNotFoundError:
    api_key = input("Please enter the API key: ")
    with open('API_KEY', 'w') as outf:
        outf.write(api_key)

time.sleep(3)
guild = input("ENTER A GUILD NAME: ")

gurl = ("https://api.hypixel.net/guild?key=" + api_key + "&name=" + guild)
g = requests.get(gurl)
g = g.json()

print('------------------------------------------')
for i in range(len(g['guild']['members'])):
  uuid = g['guild']['members'][i]['uuid']

  x = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
  x = x.json()

  expHistory = g['guild']['members'][i]['expHistory']
  print(f"{x['name']} Has gained {sum(expHistory.values())} GEXP in the last 7 days\n")


input()
