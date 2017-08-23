dataset found via http://dataportals.org/search

URL = "https://opendata.paris.fr/api/records/1.0/search/?dataset=stations-velib-disponibilites-en-temps-reel

We fetch each bike-station info individually, on each call to datasource.next()
The opendata.paris.fr API can return all bike-stations data in a single call,
however, this does not match well the injectors device-oriented architecture.
