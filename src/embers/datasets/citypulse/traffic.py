from ..lib.downloader import Downloader
from ..lib.descriptor import Descriptor

class Traffic(object):

    tarball = "traffic.json"
    metadata = "traffic_metadata.json"

    def __init__(self):
        self.tarball = Descriptor(__package__, self.tarball)
        self.metadata = Descriptor(__package__, self.metadata)

    def download(self):
        wget = Downloader(self.tarball.download_url)
        wget.download()
        wget.extract()
        wget = Downloader(self.metadata.download_url)
        wget.download()


    def __iter__(self):
        return self

    def next(self):
        raise StopIteration()
