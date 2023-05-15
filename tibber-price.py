import environment
from tibber_api import Tibber
import os
import sqlite3

r = Tibber(os.environ['API_KEY'])
conn = sqlite3.connect('powerprice.db')
db = conn.cursor()

get_price = r.req_price()
current_price = get_price['data']['viewer']['homes'][0]['currentSubscription']['priceInfo']



for each in current_price['today']:
    query = f'INSERT OR IGNORE INTO price2 (year, month, day, hour, total, energy, tax) VALUES ({each["startsAt"][0:4]}, {each["startsAt"][5:7]}, {each["startsAt"][8:10]}, {each["startsAt"][11:13]}, {each["total"]}, {each["energy"]}, {each["tax"]});'
    db.execute(query)
    conn.commit()

for each in current_price['tomorrow']:
    query = f'INSERT OR IGNORE INTO price2 (year, month, day, hour, total, energy, tax) VALUES ({each["startsAt"][0:4]},{each["startsAt"][5:7]},{each["startsAt"][8:10]},{each["startsAt"][11:13]},{each["total"]}, {each["energy"]}, {each["tax"]});'
    db.execute(query)
    conn.commit()

