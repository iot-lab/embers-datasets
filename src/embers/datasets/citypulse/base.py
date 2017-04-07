from ..lib.downloader import Downloader
from ..lib.descriptor import Descriptor

import os
import csv

DEST_DIR = __package__


class Datasource():

    def __init__(self):
        self.sources = {}

    def get_source(self, device_id):
        try:
            it = self.sources[device_id]
        except KeyError:
            it = self.Source(device_id)
            self.sources[device_id] = it
        return it

    Source = None



class FileDatasource(Datasource):

    tarball = None
    metadata = None
    source_dir = None

    def __init__(self):
        self.tarball = Descriptor(__package__, self.tarball)
        self.metadata = Descriptor(__package__, self.metadata)
        Datasource.__init__(self)

    def download(self):
        if os.path.isdir(os.path.join(DEST_DIR, self.source_dir)):
            return False
        orig_dir = os.path.abspath(os.curdir)
        os.path.isdir(DEST_DIR) or os.mkdir(DEST_DIR)
        os.chdir(DEST_DIR)
        self._download()
        os.chdir(orig_dir)

    def _download(self):
        wget = Downloader(self.tarball.download_url)
        wget.download()
        wget.extract()
        wget = Downloader(self.metadata.download_url)
        wget.download()



class IndexedFileSource():

    source_dir = None
    source_filename = None

    def __init__(self, device_id):
        index = { self.key: self.index[device_id] }
        fd = open(os.path.join(DEST_DIR, self.source_dir,
                  self.source_filename.format(**index)))
        self.reader = csv.DictReader(fd)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next()
