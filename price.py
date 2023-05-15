import sqlite3
from contextlib import closing
from datetime import date, datetime, timedelta
import json
class Pris:


	def dbquery(self, db_name, query):
		with closing(sqlite3.connect(db_name)) as con, con, \
			closing(con.cursor()) as cur:
			cur.execute(query)
			return cur.fetchall()

	def naa(self):
		this_year = date.today().year
		this_month = date.today().month
		this_day = date.today().day
		this_hour = datetime.today().hour
		query = f"SELECT energy FROM price2 WHERE year = {this_year} AND month = {this_month} AND day = {this_day} AND hour = {this_hour}"
		result = self.dbquery('/home/tibber/powerprice.db', query)
		price = {"kr":result[0][0]}
		return price

	def idag(self):
		this_year = date.today().year
		this_month = date.today().month
		this_day = date.today().day
		query = f"SELECT  hour, energy FROM price2 WHERE year = {this_year} AND month = {this_month} AND day = {this_day}"
		result = self.dbquery('/home/tibber/powerprice.db', query)
		rdict = {}
		for row in result:
			rdict[row[0]] = row[1]
		return rdict

	def imorgen(self):
		dato = date.today() + timedelta(days=1)
		this_year = dato.year
		this_month = dato.month
		this_day = dato.day
		query = f"SELECT hour, energy FROM price2 WHERE year = {this_year} AND month = {this_month} AND day = {this_day}"
		result = self.dbquery('/home/tibber/powerprice.db', query)
		rdict = {}
		for row in result:
			rdict[row[0]] = row[1]
		return rdict

	def maned(self):
		this_year = date.today().year
		this_month = date.today().month
		query = f"SELECT avg(energy) FROM price2 WHERE year = {this_year} AND month = {this_month}"
		result = self.dbquery('/home/tibber/powerprice.db', query)[0][0]
		return result

	def undermonthmedian(self):
		pass
