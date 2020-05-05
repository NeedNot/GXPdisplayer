import requests
import time
from colorama import init
from termcolor import colored

try:
    with open('API_KEY') as inf:
        api_key = inf.read()
except FileNotFoundError:
    api_key = input("Please enter your API key: ")
    with open('API_KEY', 'w') as outf:
        outf.write(api_key)

time.sleep(1)
guild = input("ENTER A GUILD NAME: ")

g = requests.get("https://api.hypixel.net/guild?key=" + api_key + "&name=" + guild)
g = g.json()

print('------------------------------------------')
for i in range(len(g['guild']['members'])):
  uuid = g['guild']['members'][i]['uuid']

  x = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid)
  x = x.json()
  name = x['name']

  for names in name:
    name = (f"{name: <16}")
  expHistory = expHistory = g['guild']['members'][i]['expHistory']
  expHistory = sum(expHistory.values())
  init()

  if (int(expHistory) >= 0):
    color = 'red'
  if (int(expHistory) >= 10000):
    color = 'yellow'
  if (int(expHistory) >= 100000):
    color = 'green'
  if (int(expHistory) >= 200000):
    color = 'cyan'

  name = colored(name, color)
  expHistory = "{:,}".format(sum(g['guild']['members'][i]['expHistory'].values()))
  expHistory = colored(expHistory, color)

  print(f"{name} Has gained {expHistory} GEXP in the last 7 days\n")


input()
