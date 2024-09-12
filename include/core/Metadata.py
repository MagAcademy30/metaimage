import exifread
from PIL import ExifTags, Image

class Metadata:
	# Метаданные
	_iso = "0" # ISO
	_shutter_speed = "0" # Скорость затрова
	_aperture = "0" # Диафрагма
	_focal_lenght = "0" # ФФ (Фокусное растояние)
	_rotation = 0 # Угол поворота

	def __init__(self, image_path):
		image = Image.open(image_path)

		# Основное
		with open(image_path, "rb") as image_file:
			tags = exifread.process_file(image_file)
			for tag in tags.keys():
				if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
					# В метаданных бывает такое что там дробные числа, и их нужно считать

					if tag == "EXIF FocalLength":
						focal_lenght_drobe = str(tags[tag]).split("/")
						if len(focal_lenght_drobe) > 1: # Дробь
							self._focal_lenght = str(int(focal_lenght_drobe[0]) / int(focal_lenght_drobe[1]))
						else:
							self._focal_lenght = str(tags[tag])

					elif tag == "EXIF ISOSpeedRatings":
						self._iso = str(tags[tag])

					elif tag == "EXIF ExposureTime":
						shutter_speed_drobe = str(tags[tag]).split("/")
						if len(shutter_speed_drobe) > 0 and int(shutter_speed_drobe[0]) > 1: # Дробь
							self._shutter_speed = "1/"+str(int(1/(int(shutter_speed_drobe[0]) / int(shutter_speed_drobe[1]))))
						else:
							self._shutter_speed = str(tags[tag])

					elif tag == "EXIF FNumber":
						aperture_drobe = str(tags[tag]).split("/")
						if len(aperture_drobe) > 1: # Дробь
							self._aperture = str(float(aperture_drobe[0]) / float(aperture_drobe[1]))
						else:
							self._aperture = str(tags[tag])

			exif = image.getexif()
			for tag, value in exif.items():
				if ExifTags.TAGS.get(tag) == "Orientation":
					if value == 3:
						self._rotation = 180
					elif value == 6:
						self._rotation = 270
					elif value == 8:
						self._rotation = 90

	def getISO(self):
		return self._iso

	def getShutterSpeed(self):
		return self._shutter_speed

	def getAperture(self):
		return self._aperture

	def getFocalLenght(self):
		return self._focal_lenght

	def getRotation(self):
		return self._rotation