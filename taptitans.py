#!/usr/bin/env python3
from ppadb.client import Client
import model

client = Client(host="127.0.0.1", port=5037)
devices = client.devices()

if len(devices) == 0:
    print("No device connected")
    quit()
    
device = devices[0]

game = model.Game(device)
game.play()