# This module gets coordinates of twitter users
# Renders a map of followers
import folium
from geopy.geocoders import Nominatim


def get_locations_dict(data):
    """
    Function to find the coordinates of users' locations
    :param data: the list of dictionaries with users' data
    :return: dictionary {location: coordinates}
    """
    locations_dict = {}
    locations = []
    for user in data:
        locations.append(user.get('location'))

    for location in locations:
        if location not in locations_dict:  # to prevent repetition of same locations
            try:
                geolocator = Nominatim()
                coordinates = geolocator.geocode(location, timeout=5)
                locations_dict[location] = (coordinates.latitude, coordinates.longitude)
            except AttributeError:  # if failed to find such location
                pass
    return locations_dict


def create_map(data, locations_dict):
    """
    Creates map
    :param data: the list of dictionaries with users' data
    :param locations_dict: dictionary {location: coordinates}
    :return: None
    """
    followers_map = folium.Map()
    try:
        for user in data:
            location = user.get('location')
            coordinates = locations_dict[location]
            info = user.get('name') + '\n' + location + '\n' + user.get('profile_image_url')

            followers_map.add_child(folium.Marker(location=[float(coordinates[0]), float(coordinates[1])],
                                                  popup=folium.Popup(info, parse_html=True),
                                                  icon=folium.Icon()))
    except KeyError:
        pass
    followers_map.save("templates/Followers.html")

