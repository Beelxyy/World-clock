import pytz
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def get_country_time(country_name):
    # Get the coordinates of the country
    geolocator = Nominatim(user_agent="timezone_finder")
    try:
        location = geolocator.geocode(country_name)
        
        if not location:
            return "Country not found. Please check the name and try again."

        latitude = location.latitude
        longitude = location.longitude

        # Find the timezone of the country using latitude and longitude
        timezone_finder = TimezoneFinder()
        timezone_str = timezone_finder.timezone_at(lng=longitude, lat=latitude)

        if not timezone_str:
            return "Timezone not found for this country."

        # Get the current time in that timezone
        timezone = pytz.timezone(timezone_str)
        time_in_country = datetime.now(timezone)

        return (f"Current time in {country_name} ({timezone_str}) is: "
                f"{time_in_country.strftime('%Y-%m-%d %H:%M:%S')}")
                
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Ask for the country name
    country_name = input("Enter the name of the country: ")
    print(get_country_time(country_name))
