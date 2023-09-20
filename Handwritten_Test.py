!pip
install
pytesseract
! apt
install
tesseract - ocr
libtesseract - dev
libmagickwand - dev
from IPython.display import HTML, clear_output

clear_output()
! pip
install
pytesseract
wand
opencv - python
clear_output()
from PIL import Image
import pytesseract
import cv2
import numpy as np
from pytesseract import Output
import re

image = Image.open('handwrittensample.png')
image = image.resize((960, 540))
image.save('sample.png')
image

custom_config = r'-l eng --oem 3 --psm 6'
text = pytesseract.image_to_string(image, config=custom_config)
print(text)
This is a
handwritten
example
Write as good
aS
you
Can.

try:
    text = pytesseract.image_to_string(image, lang="eng")
    characters_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
    new_string = text
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")
    print(new_string)
except IOError as e:
    print("Error (%s)." % e)
This is a
handwritten
example

Write as good
aS
you
Can.

image = cv2.imread('sample.png')


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray = get_grayscale(image)
Image.fromarray(gray)


def remove_noise(image):
    return cv2.medianBlur(image, 5)


noise = remove_noise(gray)
Image.fromarray(gray)


def thresholding(image):
    # source image,  grayscale image
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


thresh = thresholding(gray)
Image.fromarray(thresh)


def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


erode = erode(gray)
Image.fromarray(erode)


def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


opening = opening(gray)
Image.fromarray(opening)


def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


match = match_template(gray, gray)
match
array([[0.99999946]], dtype=float32)
from google.colab.patches import cv2_imshow

img = cv2.imread('sample.png')
h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
Image.fromarray(img)
cv2_imshow(img)

!pip
install
tesserocr
from tesserocr import PyTessBaseAPI, RIL

with PyTessBaseAPI(psm=6, oem=1) as api:
    level = RIL.SYMBOL
    api.SetImageFile('sample.png')
    api.Recognize()
    ri = api.GetIterator()
    while True:
        letter = ri.GetUTF8Text(level)
        boxes = ri.BoundingBox(level)
        print(letter, "letter")
        print(boxes, "coordinates")
        if not ri.Next(level):
            break