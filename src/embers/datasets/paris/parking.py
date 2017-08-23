import requests

URL = "https://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel&rows=1&start={device_id}"

class Parking:

    sources = {}

    def get_source(self, device_id):
        try:
            it = self.sources[device_id]
        except KeyError:
            it = _it()
            it.url = URL.format(device_id=device_id)
            self.sources[device_id] = it

        return it

    def check_device_id(device_id):
        device_id = int(device_id)
        assert device_id >= 0
        assert device_id < 1226


class _it:
    url = None

    def next(self):
        try:
            json = requests.get(self.url).json()
            data = json["records"][0]["fields"]
        except Exception as e:
            data = "error fetching data: " + e

        return { "data": data }
