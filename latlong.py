import pandas as pd 
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import unidecode # For replacing special characters

# Creating the Nominatim object
nom = Nominatim()

# Geocoder Timed Out Error Handling
def do_geocode(address):
    try:
        return nom.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)


# Reading the CSV that contains your data
data = pd.read_csv("C:\\Users\\schaturvedi\\Desktop\\Python\\data.csv", encoding='latin-1')

# Writing a function to remove the accented characters
def strip_accents(text):
		text = unidecode.unidecode(text)
		return str(text)

# Removing the accented characters
data["Address"] = data["City"].apply(strip_accents)


# Merging the City & Country to make a Single Address
data["Address"] = data["Address"]+", "+data["Country"]

# Applying the geocode on our pandas DataFrame
data["Coordinates"] = data["Address"].apply(do_geocode)

# Extracting the Latitude
data["Latitude"] = data["Coordinates"].apply(lambda x: x.latitude if x != None else None)

# Extracting the Longitude
data["Longitude"] = data["Coordinates"].apply(lambda x: x.longitude if x != None else None)

# Writing the file to CSV 
data.to_csv("LatLong.csv")


