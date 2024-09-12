import os, exifread

from include.const import *
from include.config.Config import *
from include.core.Metadata import *
from PIL import Image, ImageFont, ImageDraw

def main():
	path = os.path.abspath(".") + "/"

	print("███╗░░░███╗███████╗████████╗░█████╗░██╗███╗░░░███╗░█████╗░░██████╗░███████╗")
	print("████╗░████║██╔════╝╚══██╔══╝██╔══██╗██║████╗░████║██╔══██╗██╔════╝░██╔════╝")
	print("██╔████╔██║█████╗░░░░░██║░░░███████║██║██╔████╔██║███████║██║░░██╗░█████╗░░")
	print("██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░")
	print("██║░╚═╝░██║███████╗░░░██║░░░██║░░██║██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗")
	print("╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝")
	print("                               Версия %s                                   \n" % VERSION)
	config = Config()
	offset = config.config.data["meta_offset"].split(",")
	offset = (int(offset[0]), int(offset[1]))
	with open(path+"metainfo.txt", "r", encoding="utf-8") as metainfo_file:
		metainfo_sample = metainfo_file.read()

	images = []
	for image_name in os.listdir(path+"photos"):
		if os.path.isfile(path+"photos/"+image_name):
			images.append(image_name)

	if (len(images) > 0):
		print("Используется шрифт: %s" % config.config.data["font"])
		print("Обнаруженно %s фотографии\n" % str(len(images)))

		for i in range(len(images)):
			print("Обработка %s из %s (%s)" % (i+1, len(images), images[i]))
			metadata = Metadata(path+"photos/"+images[i])
			metainfo = ["f/%s" % metadata.getAperture(), 
						"%s" % metadata.getShutterSpeed(), 
						"%smm" % metadata.getFocalLenght(), 
						"ISO %s" % metadata.getISO()]

			image = Image.open(path+"photos/"+images[i]).convert("RGBA")
			image = image.rotate(metadata.getRotation(), expand=True)
			image_text_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
			image_draw = ImageDraw.Draw(image)
			image_text_layer_draw = ImageDraw.Draw(image_text_layer)
			font_size = int(config.config.data["meta_size"])
			font = ImageFont.truetype(path+config.config.data["font"], font_size)

			for a in range(len(metainfo)):
				text_pos = [0, 0]
				config_pos_split = config.config.data["meta_position"].split("-")

				if config_pos_split[0] == "left":
					text_pos[0] = offset[0]
				elif config_pos_split[0] == "right":
					text_pos[0] = image.size[0]-font.getlength(metainfo[a])-offset[0] # fixme!!

				if config_pos_split[1] == "up":
					text_pos[1] = ((font_size+int(config.config.data["meta_gap_beetwen_lines"]))*a)+offset[1]
				elif config_pos_split[1] == "down":
					text_pos[1] = image.size[1]-((font_size+int(config.config.data["meta_gap_beetwen_lines"]))*int(a+1))-offset[1]

				image_text_layer_draw.text((text_pos[0], text_pos[1]), metainfo[a], (255, 255, 255, int(config.config.data["meta_opacity"])), font=font)

			split_layers = Image.alpha_composite(image, image_text_layer)
			split_layers.convert("RGB").save(path+"photos/out/"+images[i], quality=100, subsampling=0)

		print("\nГотово.")

	else:
		print("Нет фотографий! Как так то?")

if __name__ == "__main__":
	main()