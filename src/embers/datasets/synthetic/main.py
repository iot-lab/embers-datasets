class Synthetic:

    sources = {}

    def get_source(self, device_id):
        try:
            it = self.sources[device_id]
        except KeyError:
            it = _it()
            it.device_name = "{}_{}".format(
                self.__class__.__name__,
                device_id)
            self.sources[device_id] = it

        return it


class _it:
    device_name = None
    event_nb = 0

    def next(self):
        self.event_nb += 1
        data = "{}.{}".format(
                self.device_name,
                self.event_nb)

        return { "data": data }

class Traffic(Synthetic): pass

class Parking(Synthetic): pass

class Pollution(Synthetic): pass
