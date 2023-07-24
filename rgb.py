import time
from rpi_ws281x import PixelStrip, Color
import argparse
 
LED_COUNT = 60        
LED_PIN = 18          # DI to GPIO18
 
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

GREEN = Color(102, 255, 102)
ORANGE = Color(255, 153, 51)
RED = Color(255, 41, 41)
PURPLE = Color(255, 0, 255)

def colorWipe(strip, color, wait_ms=20):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
 
def currSecond():
    return int(time.time()) % 60

def currMinute():
    return int(time.time() / 60 % 60)

def clockTick(strip, bg_color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, bg_color)
    while True:
        blink_pos = currMinute()
        strip.setPixelColor(blink_pos, PURPLE)
        strip.show()
        time.sleep(0.8)
        strip.setPixelColor(blink_pos, Color(0, 0, 0))
        strip.show()
        time.sleep(0.2)
        strip.setPixelColor(blink_pos, bg_color)
 

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
 
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
 
    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
 
    try:
        while True:
            clockTick(strip, GREEN)
 
    except:
        colorWipe(strip, Color(0, 0, 0), 100)

