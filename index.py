import requests

r = requests.get('https://api.hypixel.net/guild?keyKEY5&name=GUILD')
x = r.json()

if len(x['guild']['members']) == 0:
  sys.exit()

member0 = x['guild']['members'][0]
print(len(x['guild']['members']))

uuidURL = "https://sessionserver.mojang.com/session/minecraft/profile/" + member0['uuid']
uuidURL = requests.get(uuidURL).json()

total0 = 0
for exp_earned in member0['expHistory'].values():
    total0 += exp_earned
total0 = '{:,}'.format(total0)


print("%s past 7 days GXP: %s." % (uuidURL['name'], total0))


total1 = 0

if len(x['guild']['members']) == 0:
  sys.exit()

member1 = x['guild']['members'][1]
uuidURL = "https://sessionserver.mojang.com/session/minecraft/profile/" + member1['uuid']
uuidURL = requests.get(uuidURL).json()


for exp_earned in member1['expHistory'].values():
    total1 += exp_earned
total1 = '{:,}'.format(total1)


print("%s past 7 days GXP: %s." % (uuidURL['name'], total1))
