#!/usr/bin/env python3
# Prototype
# Do Python prototyping

import requests

def availableShips(passengerCount):
    """
    Uses the Star Wars API to return the list of ships that can hold
        passengerCount number of passengers

    parameters:
        passengerCount [int]:
            the number of passenger the ship must be able to carry

    returns:
        [list]: all ships that can hold that many passengers
    """

    if type(passengerCount) is not int:
            raise TypeError(
                "passengerCount must be a positive number of passengers")
    if passengerCount < 0:
            raise ValueError(
                "passengerCount must be a positive number of passengers")

    base_url = 'https://swapi-api.hbtn.io/api/starships/'
    ships = []
    response = requests.get(base_url).json()

    for ship in response['results']:
        passengers = ship.get('passengers').replace(",", "")
        if passengers != "n/a" and passengers != "unknown":
            if int(passengers) >= passengerCount:
                ships.append(ship.get('name'))
    return ships 