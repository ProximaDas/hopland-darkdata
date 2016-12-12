from PIL import Image
from pytesseract import image_to_string
import os

for files in os.listdir("."):
	if files.endswith(".jpg"):
		print(image_to_string(Image.open(files)))
