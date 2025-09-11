# File Name: main.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import requests

#= Classes =#

class HomeAssistantClient:
    # Initialize the plugin
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    # Turn on any given light
    def turn_on_light(self, entity_id: str, brightness: int = None):
        """
        Turn on any given light, when provided the entity ID
        :param entity_id: light.light_1
        :param brightness:
        :return: The Returned Data from HA
        """
        url = f"{self.base_url}/api/services/light/turn_on"
        data = {"entity_id": entity_id}
        if brightness is not None:
            data["brightness"] = brightness
        resp = requests.post(url, headers=self.headers, json=data)
        return resp.json()

    # Turn off any given light
    def turn_off_light(self, entity_id: str):
        """
        Turn off any given light, when provided the entity ID
        :param entity_id: light.light_1
        :return: The Returned Data from HA
        """
        url = f"{self.base_url}/api/services/light/turn_off"
        data = {"entity_id": entity_id}
        resp = requests.post(url, headers=self.headers, json=data)
        return resp.json()

    # Set a scene preset from HA
    def activate_scene(self, scene_id: str):
        """
        Activate a scene, to change the current parameters set in the devices that are found within that scene.
        :param scene_id: scene.lighting_scene_1
        :return: The Returned Data from HA
        """
        url = f"{self.base_url}/api/services/scene/turn_on"
        data = {"entity_id": scene_id}
        resp = requests.post(url, headers=self.headers, json=data)
        return resp.json()

    # Set the brightness of any given light
    def set_brightness(self, entity_id: str, brightness: int):
        """
        Change the brightness of any given light, when provided the entity ID and the brightness value ranging from 0 to 255 (0 is OFF)
        :param entity_id: light.light_1
        :param brightness: 128
        :return: The Returned Data from HA
        """
        url = f"{self.base_url}/api/services/light/turn_on"
        data = {"entity_id": entity_id, "brightness": brightness}
        resp = requests.post(url, headers=self.headers, json=data)
        return resp.json()

#! Main Program !#

#~ the main program goes here


#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#