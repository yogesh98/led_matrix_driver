from base import Base
from PIL import Image
from rgbmatrix import graphics
import time
import requests
import os

class CurrentWeather(Base):
    def __init__(self, *args, **kwargs):
        super(CurrentWeather, self).__init__(*args, **kwargs)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../assets/fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 255)
        apikey = os.getenv("OPENWEATHERAPIKEY")
        lat = os.getenv("LAT")
        lon = os.getenv("LON")
        print(apikey)
        print("https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+apikey)
        weather = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+apikey)
        print(weather.json())
        t_end = time.time() + 60 * 15
        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, 20, 20, textColor, "testing both")

            time.sleep(0.01)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)