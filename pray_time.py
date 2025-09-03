import requests
from requests.exceptions import HTTPError
def get_prayer_time(city,country):
    
    
    """Gets the prayer times for a city and country.

    Args:
        city: The city name.
        country: The country code.

    Returns:
        A dictionary of prayer times.
    """
    
    
    url=f" http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=8"
    try:
        response=requests.get(url)
        info=response.json()
        if "data" in info:
            prays_time=info["data"]["timings"]
            return prays_time
        else:
            return None
        
    except HTTPError as e :
        return f"Error getting prayer times: {e}"

    
    
    
city=input("city :").strip().capitalize()
country=input("country :").strip().capitalize()

if city.isalpha() and country.isalpha():
        prays_time=get_prayer_time(city,country)
        for key,value in prays_time.items():
            print(f"{key}=>{value}")
else:
    raise Exception("city or country is not a string")    
            
        

