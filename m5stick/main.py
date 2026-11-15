import M5
from M5 import *

def button_a_clicked(state):
    M5.Speaker.playWavFile("/flash/zundamon.wav")

def setup():
    M5.begin()
    M5.Speaker.setVolume(250)
    BtnA.setCallback(
        type=BtnA.CB_TYPE.WAS_CLICKED,
        cb=button_a_clicked
    )

def loop():
    M5.update()

if __name__ == "__main__":
    setup()
    while True:
        loop()
