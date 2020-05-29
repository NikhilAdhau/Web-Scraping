# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ImdbPipeline(object):
	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection (self):
		self.conn = sqlite3.connect("List.db")	
		self.curr = self.conn.cursor()

	def create_table (self):
		self.curr.execute (""" DROP TABLE IF EXISTS movies_tb""")
		self.curr.execute (""" DROP TABLE IF EXISTS series_tb""")
		#if item.get('Movies'):
		self.curr.execute("""
				create table movies_tb (Title text, Year text, Duration text, Rating text, Trailer text, More_Info text)
			""")
		self.curr.execute("""
				create table series_tb (Title text, Year text, Episodes text, Episode_Duration text,Rating text, Trailer text, More_Info text)
			""")


	def process_item(self, item, spider):
		self.store_db(item)
		return item
        
	def store_db(self, item):
		if item.get('Movies') == 1:
			self.curr.execute (""" INSERT INTO movies_tb values (?, ?, ?, ?, ?, ?)""",(
								item.get('Title'),
								item.get('Year'),
								item.get('Duration'),
								item.get('Rating'),
								item.get('Trailer'),
								item.get('Link'),

						))
		else:
			self.curr.execute (""" INSERT INTO series_tb values (?, ?, ?, ?, ?, ?, ?)""",(
								item.get('Title'),
								item.get('Year'),
								item.get('Total Episodes'),
								item.get('Episode Duration'),
								item.get('Rating'),
								item.get('Trailer'),
								item.get('Link'),

						))


		self.conn.commit()


