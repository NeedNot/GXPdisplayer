import requests

r = requests.get('https://api.hypixel.net/guild?key=PRIVET&name=GUILDNAME')
x = r.json()

member0 = x['guild']['members'][0]


uuidURL = "https://sessionserver.mojang.com/session/minecraft/profile/" + member0['uuid']
uuidURL = requests.get(uuidURL).json()

total0 = 0
for exp_earned in member0['expHistory'].values():
    total0 += exp_earned
total0 = '{:,}'.format(total0)


print("%s past 7 days GXP: %s." % (uuidURL['name'], total0))

member1 = x['guild']['members'][1]
uuidURL = "https://sessionserver.mojang.com/session/minecraft/profile/" + member1['uuid']
uuidURL = requests.get(uuidURL).json()

total1 = 0
for exp_earned in member1['expHistory'].values():
    total1 += exp_earned
total1 = '{:,}'.format(total1)


print("%s past 7 days GXP: %s." % (uuidURL['name'], total1))
