from base import IndexedFileSource
from base import FileDatasource
from base import DEST_DIR

import os
import csv


SOURCE_DIR = "traffic_june_sep" # in effect aug_sep_2014 (cf traffic.json)
SOURCE_FILENAME = "trafficData{REPORT_ID}.csv"
METADATA_FILENAME = "trafficMetaData.csv"


class FileSource(IndexedFileSource):
    source_dir = SOURCE_DIR
    source_filename = SOURCE_FILENAME
    key = "REPORT_ID"


class Traffic(FileDatasource):

    tarball = "traffic.json"
    metadata = "traffic_metadata.json"
    source_dir = SOURCE_DIR

    Source = FileSource

    def download(self):
        FileDatasource.download(self)
        self._metadata = metadata = get_traffic_metadata()
        self.Source.index = [ m[self.Source.key] for m in metadata ]

    def get_metadata(self):
        return self._metadata


def get_traffic_metadata():
    traffic_metadata = []
    with open(os.path.join(DEST_DIR, METADATA_FILENAME)) as csvfile:
        reader = csv.DictReader(csvfile)
        for metadata in reader:
            for discard in [ 'REPORT_NAME', 'RBA_ID', '_id' ]:
                del metadata[discard]
            traffic_metadata.append(metadata)

    return traffic_metadata
