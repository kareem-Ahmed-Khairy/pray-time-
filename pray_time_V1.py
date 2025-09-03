import requests
from requests.exceptions import HTTPError

def get_prayer_time(city: str, country: str) -> dict:
    """
    Gets the prayer times for a city and country.

    Args:
        city (str): The city name.
        country (str): The country name or code.

    Returns:
        dict: A dictionary of prayer times or None if failed.
    """
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=8"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        info = response.json()
        if "data" in info:
            return info["data"]["timings"]
        else:
            print("Could not get prayer times. Check city/country.")
            return None
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

def main():
    city = input("Enter city: ").strip().capitalize()
    country = input("Enter country: ").strip().capitalize()

    if not city.isalpha() or not country.isalpha():
        print("Error: city and country must only contain letters.")
        return

    prays_time = get_prayer_time(city, country)
    if prays_time:
        print(f"\nPrayer times for {city}, {country}:")
        for key, value in prays_time.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
