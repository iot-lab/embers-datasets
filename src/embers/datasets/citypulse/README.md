This is the CityPulse dataset.

	http://iot.ee.surrey.ac.uk:8080/datasets.html


Dataset descriptors:

- `traffic.json` => `_aug_sep_2014.tar.gz`, the CSV raw data archive
- `traffic_metadata.json` => the metadata
- `pollution.json` => `_aug_oct_2014.tar.gz`, the CSV raw data archive

Metadata describes 449 'reporters' (road chunks) identified by a unique
`REPORT_ID` and provides attributes such as location address, entry/exit
points GPS coordinates and distance.

Traffic data is stored in a .tar.gz file as a set of CSV files named
`trafficData<REPORT_ID>.csv`, one per 'reporter' present in the metadata.

Each of the 449 files contains 14-17k lines of timestamped traffic data.
The time resolution for this dataset is 5 minutes.  Data is real recorded
data, that is, for instance, the files do not necessarily contain exactly
one line of data for every 5 minute interval; some are missing.

Pollution data as stored in the .tar.gz file are similar to traffic data: same
file naming scheme, same number of files.  The time resolution is 5 minutes.
This dataset is generated and intends to complement the traffic dataset.
