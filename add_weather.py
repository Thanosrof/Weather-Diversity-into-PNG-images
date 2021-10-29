'''''''''''''''''''''''''''DESCRIPTION'''''''''''''''''''''''''''

''' This Python script is implemented in order to add weather conditions to 16-bit grayscale(monochrome)   '''
'''    PNG images. The script gets as input the path of the folder that the images are saved and then it   '''
'''    reads every image on that forlder. Additionally, the algorithm selects randomly from five different '''
'''    weather conditions which are "Brighter","Darker","Rainy", "Snowy","Foggy". The selected condition   '''
'''    is added to each image stored into the path folder and then it is saved as a PNG 16-bit image with  '''
'''    the same name as the original one. '''



import cv2
import numpy as np
import glob
import random 
import os
import argparse

from numpy.lib.type_check import imag

''' Reads the path for the folder saved the images'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required = True, help = "path to images")
args = vars(ap.parse_args())

inputFolder = os.path.sep.join([args["image"]])
folderlen = len(inputFolder)

''' for used to ascess every image with the png extension file of the folder'''
for img in glob.glob(inputFolder + "/*.png"):

    ''' Reads and store the image and selects randomly one of the 5 weather conditions'''
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    randomWeather = random.choice(["Brighter","Darker","Rainy", "Snowy","Foggy"])

    ''' If is used to seperate the 5 different conditions''' 
    if randomWeather == "Brighter" :

        ''' Adds brightness to the image and saves it'''
        randomBrightness = random.randint(10,80)
        bright = np.ones(image.shape, dtype = "uint8") * randomBrightness
        brightIncrease = cv2.add(image,bright)
        brightIncrease = ((brightIncrease + 1 ) * 256 ) -1
        cv2.imwrite(inputFolder + img[folderlen:],brightIncrease)

    elif randomWeather == "Darker" :
        
        ''' Subtracts brightness of the image and saves it'''
        randomDarkness = random.randint(10,80)
        bright = np.ones(image.shape, dtype = "uint8") * randomDarkness
        brightDecrease = cv2.subtract(image,bright)
        brightDecrease = ((brightDecrease + 1 ) * 256 ) -1
        cv2.imwrite(inputFolder + img[folderlen:],brightDecrease)

    elif randomWeather == "Rainy":

        ''' Adds rain drops to the image and saves it'''
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

        ''' Adds snow drops to the image and saves it'''
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

         ''' Blurs the image likewise fog and saves it'''
        foggy_image= cv2.blur(image,(10,10))
        foggy_image = ((foggy_image + 1 ) * 256 ) -1
        cv2.imwrite(inputFolder + img[folderlen:],foggy_image)
        
        
    print(img + "Done")
