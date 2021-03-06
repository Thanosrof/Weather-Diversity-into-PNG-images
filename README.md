# Adding weather conditons to PNG grayscale images

This Python code is a script that I implemented for my thesis project. This script reads grayscale PNG images that are stored into a folder and adds weather conditions. 

There are five weather conditions that the program selects randomly from:
1) Sunny weather 
2) Cloudy weather
3) Rainy 
4) Snowy
5) Foggy 


### Requirements

- Python >= 3.8.10
- OpenCv 4.2.0
- Numpy 1.19.5
 
## Usage

* python3 add_weather.py -i /Path/to/folder/

|Flag                  | Description
|----------------------|--------------------------------------------------------
| -i                  | Path to the folder containing the images 


## Examples


# Example 1

Original Image <br/>
<img src="images/original/1_original.png" width="700" >

Image with added snow weather condition<br/>
<img src="images/weather_diversity/1_waether.png"  width="700">


# Example 2


Original Image <br/>
<img src="images/original/2_original.png" width="700" >

Image with added cloudly weather condition, cloudy weather so darker image<br/>
<img src="images/weather_diversity/2_waether.png" width="700" >

# Example 3


Original Image<br/>
<img src="images/original/3_original.png" width="700">

Image with added fog condition<br/>
<img src="images/weather_diversity/3_waether.png" width="700" >


## Acknowledgement

This script was part of my master's thesis. My thesis was part of a project at Revere lab at Chalmers university of technology. The images shown above are part of the dataset that the researchers at Revere lab have established. If you want to have access and get sample of the dataset please visit the official site of Revere at [Reeds](https://reeds.opendata.chalmers.se/)
