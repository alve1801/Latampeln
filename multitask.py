#! /bin/bash/
#
import RPi.GPIO as G
import time as t
from _thread import start_new_thread
auto_rot = 4
auto_gelb = 17
auto_grün = 18
fahrrad_rot = 27
fahrrad_grün = 22
auto_rechts = 23
auto_sensor = 24
fahrrad_sensor = 25
G.setmode(G.BCM)
G.setup(auto_rot, G.OUT)
G.setup(auto_gelb, G.OUT)
G.setup(auto_grün, G.OUT)
G.setup(fahrrad_rot, G.OUT)
G.setup(fahrrad_grün, G.OUT)
G.setup(auto_rechts, G.OUT)
G.setup(auto_sensor, G.IN)
G.setup(fahrrad_sensor, G.IN)
G.output(auto_rot, False)
G.output(auto_gelb, False)
G.output(auto_grün, False)
G.output(fahrrad_rot, False)
G.output(fahrrad_grün, False)
G.output(auto_rechts, False)
G.output(auto_rot, True)
G.output(fahrrad_rot, True)
def auto():
  while 1:
    if G.input(auto_sensor):
      G.output(auto_rot, False)
      G.output(auto_gelb, True)
      t.sleep(1.5)
      G.output(auto_gelb, False)
      G.output(auto_grün, True)
      t.sleep(5)
      G.output(auto_grün, False)
      G.output(auto_gelb, True)
      G.output(auto_rot, True)
      t.sleep(1.5)
      G.output(auto_gelb, False)
def fahrrad():
  while 1:
    if G.input(fahrrad_sensor):
      G.output(auto_rechts, True)
      G.output(fahrrad_rot, False)
      G.output(fahrrad_grün, True)
      t.sleep(5)
      G.output(fahrrad_grün, False)
      G.output(fahrrad_rot, True)
      G.output(auto_rechts, False)
start_new_thread(auto, ())
start_new_thread(fahrrad, ())
while 1:
    