#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../assets/fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 255)
        my_text = self.args.text
        response = requests.get("http://worldtimeapi.org/api/timezone/America/New_York")
        print(response.json())
        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, 20, 20, textColor, my_text)

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
