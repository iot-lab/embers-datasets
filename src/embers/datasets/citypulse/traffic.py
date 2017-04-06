from ..lib.downloader import Downloader
from ..lib.descriptor import Descriptor

import os
import csv

DEST_DIR = __package__

SOURCE_DIR = "traffic_june_sep" # in effect aug_sep_2014 (cf traffic.json)
SOURCE_FILENAME = "trafficData{REPORT_ID}.csv"
METADATA_FILENAME = "trafficMetaData.csv"


class Traffic(object):

    tarball = "traffic.json"
    metadata = "traffic_metadata.json"

    source_dir = SOURCE_DIR

    def __init__(self):
        self.tarball = Descriptor(__package__, self.tarball)
        self.metadata = Descriptor(__package__, self.metadata)
        self.sources = {}

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

    def get_source(self, device_id):
        try:
            it = self.sources[device_id]
        except KeyError:
            metadata = self.get_metadata()[device_id]
            it = self.FileSource(metadata["REPORT_ID"])
            it.metadata = metadata
            self.sources[device_id] = it
        return it

    def get_metadata(self):
        if not self._metadata:
            self._metadata = get_traffic_metadata()
        return self._metadata

    _metadata = []


class FileSource():

    source_dir = SOURCE_DIR
    source_filename = SOURCE_FILENAME

    def __init__(self, report_id):
        fd = open(os.path.join(DEST_DIR, self.source_dir,
                  self.source_filename.format(REPORT_ID=report_id)))
        self.reader = csv.DictReader(fd)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next()

Traffic.FileSource = FileSource


def get_traffic_metadata():
    traffic_metadata = []
    with open(os.path.join(DEST_DIR, METADATA_FILENAME)) as csvfile:
        reader = csv.DictReader(csvfile)
        for metadata in reader:
            for discard in [ 'REPORT_NAME', 'RBA_ID', '_id' ]:
                del metadata[discard]
            traffic_metadata.append(metadata)

    return traffic_metadata
