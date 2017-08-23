dataset found via http://dataportals.org/search

URL = "https://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel

We fetch each bike-station info individually, on each call to datasource.next()

The opendata.paris.fr API can return all bike-stations data in a single call,
using parameter rows=1226 - there are 1226 bike-stations as of Aug. 2017.
However, this does not match well the injectors device-oriented architecture.

Should performance become an issue, we could switch to fetching all data for
all stations at once, limit server requests to one per minute and synchronize
each datasource iterator to the single response.
