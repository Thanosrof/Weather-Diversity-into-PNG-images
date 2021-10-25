import cv2
import numpy as np
import glob
import random 
import os
import argparse

from numpy.lib.type_check import imag


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required = True, help = "path to images")
args = vars(ap.parse_args())

inputFolder = os.path.sep.join([args["image"]])
folderlen = len(inputFolder)

for img in glob.glob(inputFolder + "/*.png"):

    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    randomWeather = random.choice(["Brighter","Darker","Rainy", "Snowy","Foggy"])

    if randomWeather == "Brighter" :

        randomBrightness = random.randint(10,80)
        bright = np.ones(image.shape, dtype = "uint8") * randomBrightness
        brightIncrease = cv2.add(image,bright)
        brightIncrease = ((brightIncrease + 1 ) * 256 ) -1
        cv2.imwrite(inputFolder + img[folderlen:],brightIncrease)

    elif randomWeather == "Darker" :

        randomDarkness = random.randint(10,80)
        bright = np.ones(image.shape, dtype = "uint8") * randomDarkness
        brightDecrease = cv2.subtract(image,bright)
        brightDecrease = ((brightDecrease + 1 ) * 256 ) -1
        cv2.imwrite(inputFolder + img[folderlen:],brightDecrease)

    elif randomWeather == "Rainy":

        rain = []
        rain_drops = random.randint(1000,2000)
        random_number = random.randint(-10,10)
        for elem in range(rain_drops):
            if random_number < 0 :
                x = random.randint(random_number,image.shape[1])
            else:
                x = random.randint(random_number,image.shape[1] - random_number)
            rain.append((x,random.randint(0,image.shape[0]- 5)))
        for drop in rain:
            start_point = (drop[0],drop[1])
            end_point = (drop[0] + random_number,drop[1] + 5)
            color = (175,195,204)
            cv2.line(image,start_point,end_point,color,5)
        image = cv2.blur(image,(7,7))
        rainy_image = cv2.add(image,70)
        rainy_image = ((rainy_image + 1 ) * 256 ) -1
        cv2.imwrite(inputFolder + img[folderlen:],rainy_image)

    elif randomWeather == "Snowy":

        rain = []
        rain_drops = random.randint(1000,2000)
        random_number = random.randint(-2,2)
        for elem in range(rain_drops):
            if random_number < 0 :
                x = random.randint(random_number,image.shape[1])
            else:
                x = random.randint(random_number,image.shape[1] - random_number)
            rain.append((x,random.randint(0,image.shape[0]- 2)))
        for drop in rain:
            start_point = (drop[0],drop[1])
            end_point = (drop[0] + random_number,drop[1] + 2)
            color = (255,250,250)
            cv2.line(image,start_point,end_point,color,2)
        image = cv2.blur(image,(5,5))
        snowy_image = cv2.add(image,70)
        snowy_image = ((snowy_image + 1 ) * 256 ) -1
        cv2.imwrite(inputFolder + img[folderlen:],snowy_image)

    elif randomWeather == "Foggy":

        foggy_image= cv2.blur(image,(10,10))
        foggy_image = ((foggy_image + 1 ) * 256 ) -1
        cv2.imwrite(inputFolder + img[folderlen:],foggy_image)
    print(img + "Done")