from homebridge import HomeBridgeController as HBC
import sqlite3
from datetime import date, datetime
import time

controller = HBC(host="10.0.0.176", port="51427", auth="911-53-177")

this_hour = datetime.today().hour

conn = sqlite3.connect('powerprice.db')
db = conn.cursor()

this_day = date.today().day
this_hour = datetime.today().hour
this_month = date.today().month
this_year = date.today().year

avg_price = db.execute(f'SELECT avg(energy) from price2 where year = {this_year} AND month = {this_month}').fetchall()[0][0]
current_price = db.execute(f'SELECT energy FROM price2 WHERE year = {this_year} AND month = {this_month} AND day = {this_day} AND hour = {this_hour}').fetchall()[0][0]

conn.close()

last_checked_hour = this_hour

if current_price < avg_price:
	controller.set_value("Bryter 1", True)
	controller.set_value("Bryter 2", True)
else:
	controller.set_value("Bryter 1", False)
	controller.set_value("Bryter 2", False)
