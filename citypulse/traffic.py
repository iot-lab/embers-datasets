class Traffic(object):

    descriptor = "traffic.json"
    metadata = "traffic_metadata.json"

    def __init__(self):
        pass

    def download(self):
        pass

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration()
