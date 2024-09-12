"""
		 cfgparser
Мини Библиотека для конфиг файлов.
		  By MG30
"""

import os

#Класс библиотеки
class cfgparser:
	def __init__(self, path):
		self.data = {} #Это переменная в которой хранятся данные файла в формате словаря, которые можно изменять.
		self.path = path # Путь к файлу
		self.encoding = "utf-8"

	def read(self):
		#В этой функции мы читаем и парсим конфиг файл
		file = open(self.path, "r+", encoding=self.encoding) #Открываем файл
		text = str(file.read()).split("\n") #Читаем и сразу делим на строчки
		file.close() #Закрываем файл что бы не повредить
		for line in text: #Переходим в цикл
			try:
				parsed = line.split("=", 1) #Разделяем на список по символу = ОДИН РАЗ!!
				self.data[str(parsed[0])] = str(parsed[1]) #Записываем в self.data
			except:
				pass

	def write(self):
		#В этой фунции мы записываем всё в файл из self.data
		text = "" #Создаём переменную которую будем записывать в файл

		for name in self.data: #В цикле превращяем словарь в текст
			data = self.data[name] #Получаем текст
			got = "%s=%s\n" % (name, data) #Делаем текст
			text += got #Добавляем его в главный текст для записи

		file = open(self.path, "w+", encoding=self.encoding) #Открываем файл
		file.write(text) #Записываем
		file.close() #Закрываем файл