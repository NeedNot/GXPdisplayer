import requests

r = requests.get('PRIVET URL')
x = r.json()

member0 = x['guild']['members'][0]


total0 = 0
for exp_earned in member0['expHistory'].values():
    total0 += exp_earned
total0 = '{:,}'.format(total0)


print("%s past 7 days GXP: %s." % (member0['uuid'], total0))
