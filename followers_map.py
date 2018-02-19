# This module gets coordinates of twitter users
# Renders a map of followers
import folium
from geopy.geocoders import Nominatim


def get_coordinates(data):
    """
    Function to find the coordinates of users' locations
    Modifies users dictionary
    :param data: the list of dictionaries with users' data
    """
    for user in data:
        geolocator = Nominatim()
        location = user.get('location')
        try:
            coordinates = geolocator.geocode(location, timeout=5)
            user['location'] = (coordinates.latitude, coordinates.longitude)
        except AttributeError:  # if failed to find such location
            user['location'] = 0


def create_map(data):
    """
    Creates map
    :param data: the list of dictionaries with users' data
    :return: None
    """
    followers_map = folium.Map()
    for user in data:
        location = user.get('location')
        icon_url = user.get('profile_image_url')
        icon = folium.features.CustomIcon(icon_url,icon_size=(28, 30))
        if location != 0:
            info = user.get('name')
            followers_map.add_child(folium.Marker
                                    (location=[float(location[0]), float(location[1])],
                                    popup=folium.Popup(info, parse_html=True),
                                    icon=icon))
    followers_map.save("templates/Followers.html")
