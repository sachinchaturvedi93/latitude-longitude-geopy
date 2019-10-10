# Introduction
Have you ever wanted to know the Latitude & Longitude of your home? If yes, then I am really excited to share this with you folks. You can not only find the Latitude & Longitude of your home but also a tonnes of locations together!! 

This is slow though. Requires patience :grinning:!

# How to use this
This is based on Python 3.

1. Clone or download this repository.
2. Run `pip install -r requirements.txt`.
3. Save your list of addresses in `data.csv` in `City` & `Country` columns. You can change it according to your needs.
4. Voila it gets out in `LatLong.csv`.

# Notes
1. Used `geopy` for getting the `Latitude` & `Longitude`.
2. Used `unidecode` for changing accented characters. For example, the locations mentioned in my `data.csv` file are from Costa Rica and they have a lot of accented characters in the city names.
3. Created a function `do_geocode` to handle **Geocoder Timed Out Error**. Don't forget to *import GeocoderTimedOut* using this `from geopy.exc import GeocoderTimedOut`.
4. Used `pandas` for `DataFrame` operations.
5. `data.csv` is the example of input file. `LatLong.csv` is the example of the output file.

Have Fun ! :smile:
