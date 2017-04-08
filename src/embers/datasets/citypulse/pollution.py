from base import IndexedFileSource
from traffic import Traffic


SOURCE_DIR = "pollution"
SOURCE_FILENAME = "pollutionData{REPORT_ID}.csv"


class FileSource(IndexedFileSource):
    source_dir = SOURCE_DIR
    source_filename = SOURCE_FILENAME
    key = "REPORT_ID"


class Pollution(Traffic):

    tarball = "pollution.json"
    metadata = "traffic_metadata.json"
    source_dir = SOURCE_DIR

    Source = FileSource
