import requests
import threading
import time

from embers.datasets.lib import use_fiware_format


URL = "https://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel&rows=1226"

class Parking:

    sources = {}

    def get_source(self, device_id):
        try:
            it = self.sources[device_id]
        except KeyError:
            it = _it()
            it.id = device_id
            self.sources[device_id] = it

        return it

    def check_device_id(device_id):
        device_id = int(device_id)
        assert device_id >= 0
        assert device_id < 1226


class _it:

    def next(self):
        try:
            json = get_data()
            data = json["records"][self.id]["fields"]
        except Exception as e:
            data = "error fetching data: {}".format(e)

        if use_fiware_format:
            data = to_fiware(data)

        return { "data": data }


class state:
    lock = threading.Lock()
    data = None
    timestamp = 0


def get_data():
    with state.lock:
        if state.timestamp < time.time() - 60:
            json = requests.get(URL).json()
            state.data = json
            state.timestamp = time.time()
        return state.data


def to_fiware(data):
    return {
        "id": data["name"],
        "type": "OnStreetParking",
        "dateModified": data["last_update"],
        "category": "bike station",
        "location": {
          "type": "Point",
          "coordinates": data["position"],
        },
        "address": data["address"],
        "name": data["name"],
        "chargeType": "velib", # or "other",
        "requiredPermit": "", # null
        "permitActiveHours": "", # null
        "allowedVehicleType": "bicycle",
        "extraSpotNumber": 0,
        "occupancyDetectionType": "docking station",

        "totalSpotNumber": data["bike_stands"],
        "availableSpotNumber": data["available_bike_stands"],
    }


sample_record_fields = """
    "status":"OPEN",
    "contract_name":"Paris",
    "name":"17005 - BROCHANT",
    "bonus":"False",
    "bike_stands":35,
    "number":17005,
    "last_update":"2017-09-11T11:08:44+00:00",
    "available_bike_stands":27,
    "banking":"True",
    "available_bikes":8,
    "address":"43 RUE BROCHANT - 75017 PARIS",
    "position":[
        48.8903299891,
        2.31973055993
    ]
"""
