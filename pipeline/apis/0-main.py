#!/usr/bin/python3

availableShips = __import__('0-passengers').availableShips
ships = availableShips(10)
for ship in ships:
    print(ship)