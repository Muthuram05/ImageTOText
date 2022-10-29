import pytesseract
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

folderpath="UDS 14068"
mylist=os.listdir(folderpath)
print(mylist)
for impath in mylist:
    img = Image.open(f"{folderpath}/{impath}")

#print(img)
    result = pytesseract.image_to_string(img)
    with open('abc.txt', mode='a') as file:
        file.write(result)
        print(result)
