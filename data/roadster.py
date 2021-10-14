import requests


def roadsters_requests():
    url = "https://api.spacexdata.com/v3/roadster"
    request = requests.get(url)
    data = request.json()

    print(
        f"Roadster : {data['name']} ->\n"
        f"• Launch date utc : {data['launch_date_utc']}\n"
        f"• Launch date unix : {data['launch_date_unix']}\n"
        f"• Launch mass kg : {data['launch_mass_kg']}\n"
        f"• Launch mass lbs : {data['launch_mass_lbs']}\n"
        f"• Orbit type : {data['orbit_type']}\n"
        f"• Inclination : {data['inclination']}\n"
        f"• Longitude : {data['longitude']}\n"
        f"• Speed KPH : {data['speed_kph']}\n"
        f"• Speed MPH : {data['speed_mph']}\n"
        f"• Speed KMH : {data['speed_mph'] * 1.609344}\n"
        f"• Earth distance KM: {data['earth_distance_km']}\n"
        f"• Mars distance KM : {data['mars_distance_km']}\n"
        f"• Details: {data['details']}\n"
    )
