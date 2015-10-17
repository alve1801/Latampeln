#! /bin/bash/
#
import RPi.GPIO as G
auto_rot = 4
auto_gelb = 17
auto_grün = 18
fahrrad_rot = 27
fahrrad_grün = 22
auto_rechts = 23
auto_sensor = 24
fahrrad_sensor = 25
beleuchtung_1 = 26
beleuchtung_2 = 20
beleuchtung_3 = 21
G.setmode(G.BCM)
G.setup(auto_rot, G.OUT)
G.setup(auto_gelb, G.OUT)
G.setup(auto_grün, G.OUT)
G.setup(fahrrad_rot, G.OUT)
G.setup(fahrrad_grün, G.OUT)
G.setup(auto_rechts, G.OUT)
G.setup(auto_sensor, G.IN)
G.setup(fahrrad_sensor, G.IN)
G.setup(beleuchtung_1, G.OUT)
G.setup(beleuchtung_2, G.OUT)
G.setup(beleuchtung_3, G.OUT)
G.output(auto_rot, False)
G.output(auto_gelb, False)
G.output(auto_grün, False)
G.output(fahrrad_rot, False)
G.output(fahrrad_grün, False)
G.output(auto_rechts, False)