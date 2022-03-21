#!/usr/bin/env python
from weather import CurrentWeather

# Main function
if __name__ == "__main__":
    weather = CurrentWeather()
    if (not weather.process()):
        weather.print_help()
