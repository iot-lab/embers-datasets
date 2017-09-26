dataset found via http://dataportals.org/search

URL = "https://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel

We fetch bike-station info globally for all 1226 stations and not more than
once every minute.  Each call to `datasource.next()` checks state timestamp
and returns the same data until data grows older than a minute, at which point
one of the threads fetches fresh data again.

The opendata.paris.fr API can return all bike-stations data in a single call,
using parameter rows=1226 - there are 1226 bike-stations as of Aug. 2017.

Note that individual bike-station data can be fecthed as well using parameters
start=<nb> and rows=1, which in effect returns a single record.

We used to get data on a per-station-basis as this matched well the injectors
device-oriented architecture.  However, doing so with 1226 devices quickly
hits the 100.000 API calls/day/client IP limit imposed by opendata.paris.fr.
