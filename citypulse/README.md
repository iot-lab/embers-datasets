This is the CityPulse dataset.

	http://iot.ee.surrey.ac.uk:8080/datasets.html


files:
- `traffic.json` => `_aug_sep_2014.tar.gz`, the CSV raw data archive
- `traffic_metadata.json` => the metadata
- `pollution.json` => `_aug_oct_2014.tar.gz`, the CSV raw data archive

Metadata describes 449 'reporters' (road chunks) identified by a unique
`REPORT_ID` and provides attributes such as location address, entry/exit
points GPS coordinates and distance.  We use this data, as is, to register
devices into the system ; we mirror all but the last 3 columns.

Traffic data as stored in the .tar.gz file are a set of CSV files named
`trafficData<REPORT_ID>.csv`, one per 'reporter' present in the metadata.
There are 449 files, each containing 14-17k lines of timestamped data.
The time resolution for traffic data is 5s.  Data is real recorded data.

Pollution data as stored in the .tar.gz file are similar to traffic data: same
file naming scheme, same number of files.  The time resolution is 5 minutes.
This dataset is generated, to complement the traffic dataset.
