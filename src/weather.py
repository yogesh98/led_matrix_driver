from base import Base
from PIL import Image
from rgbmatrix import graphics
import time
import requests
import os
import json


class CurrentWeather(Base):
    def __init__(self, *args, **kwargs):
        super(CurrentWeather, self).__init__(*args, **kwargs)
        self.last_pull = None
        self.weather = None

    def get_weather(self):
        if(self.last_pull is None or time.time() - self.last_pull >= 60):
            apikey = os.getenv("OPENWEATHERAPIKEY")
            lat = os.getenv("LAT")
            lon = os.getenv("LON")
            print("pulling data")
            self.weather = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+apikey).json()
            print(self.weather)
            self.last_pull = time.time()


    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        
        font = graphics.Font()
        font.LoadFont("../assets/fonts/helvR12.bdf")

        textColor = graphics.Color(255, 255, 255)

        self.get_weather()
        weather = self.weather['weather'][0]
        main = self.weather['main']
        main['temp'] = (float(main['temp']) - 273.15) * 9/5 + 32 
        print("got weather")
        img = Image.open('../assets/weather/'+weather['icon']+'.png')
        print("open image")
        img = img.convert('RGB')
        print("convert image")
        # # img.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
        print(self.weather)
        while True:
            # print("running")
            offscreen_canvas.Clear()
            offscreen_canvas.SetImage(img, -2, -6)

            graphics.DrawText(offscreen_canvas, font, 4, 30, textColor, weather['main'])            
            l = graphics.DrawText(offscreen_canvas, font, 32, 15, textColor, str(round(main['temp'],1)))
            graphics.DrawText(offscreen_canvas, font, 32+l, 13, textColor, "°")

            self.get_weather()
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            time.sleep(0.01)
