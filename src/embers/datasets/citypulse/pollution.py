from traffic import Traffic
from traffic import FileSource as FS


SOURCE_DIR = "pollution"
SOURCE_FILENAME = "pollutionData{REPORT_ID}.csv"


class FileSource(FS):
    source_dir = SOURCE_DIR
    source_filename = SOURCE_FILENAME


class Pollution(Traffic):

    tarball = "pollution.json"
    metadata = "traffic_metadata.json"
    source_dir = SOURCE_DIR

    FileSource = FileSource
