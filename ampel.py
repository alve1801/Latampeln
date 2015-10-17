#! /bin/bash/
#
import RPi.GPIO as G
import time as t
G.setmode(G.BCM)
#Autoampel rot
G.setup(4, G.OUT)
#Autoampel gelb
G.setup(17, G.OUT)
#Autoampel grün
G.setup(18, G.OUT)
#Fahrradampel rot
G.setup(27, G.OUT)
#Fahrradampel grün
G.setup(22, G.OUT)
#Autoampel Rechtsabbieger
G.setup(23, G.OUT)
#Straßenbeleuchtung
G.setup(5, G.OUT)
G.setup(6, G.OUT)
#1. Sensor
G.setup(24, G.IN)
#2. Sensor
G.setup(25, G.IN)
#alle Lampen ausschalten
G.output(4, False)
G.output(17, False)
G.output(18, False)
G.output(27, False)
G.output(22, False)
G.output(23, False)
G.output(5, False)
G.output(6, False)
#alles auf rot setzen
G.output(4, True)
G.output(27, True)
while 1:
#Autoampelschaltung
    if G.input(24):
        G.output(5, True)
        G.output(6, True)
        G.output(17, True)
        t.sleep(1.5)
        G.output(17, False)
        G.output(18, True)
        