import os

from include.config.cfgparser import *

class Config:
	def __init__(self):
		self.path = os.path.abspath(".") + "/"
		self.config = cfgparser(self.path+"config.txt")

		# Конфиг
		self.config.data["font"] = "font/CaviarDreams.ttf" # Шрифт

		self.config.data["meta_opacity"] = "255" # Прозрачность
		self.config.data["meta_size"] = "250" # Размер
		self.config.data["meta_position"] = "left-down" # Размер
		self.config.data["meta_offset"] = "50,80" # Сдвиг
		self.config.data["meta_gap_beetwen_lines"] = "0" # Пространство между линиями

		if os.path.exists(self.path+"config.txt"):
			self.config.read()
			self.config.write()
		else:
			self.config.write()