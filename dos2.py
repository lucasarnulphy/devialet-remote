import requests
import json
from discovery import list_zeroconf_devices

def build_ip_control_url(device):
    return f"http://{device['ip']}:{str(device['port'])}{device['path']}"

def get_device(device, devices, update):
    req = requests.get(url = f"{build_ip_control_url(device)}/devices/current")
    device.update(req.json())
    devices[device["deviceId"]] = device
    return devices[device["deviceId"]]

def get_system(device, systems, update):
    if (not "systemId" in device) or (not device["systemId"] in systems) or update:
        req = requests.get(url = f"{build_ip_control_url(device)}/systems/current")
        systems[device["systemId"]] = req.json()
    return systems[device["systemId"]]

def get_system_volume(device, systems_volume, update):
    if (not device["systemId"] in systems_volume) or update:
        req = requests.get(url = f"{build_ip_control_url(device)}/systems/current/sources/current/soundControl/volume")
        systems_volume[device["systemId"]] = req.json()
    return systems_volume[device["systemId"]]

def set_system_volume(device, volume):
    url = build_ip_control_url(device) + "/systems/current/sources/current/soundControl/volume"
    req = requests.post(url = url, json = {"systemVolume": volume})

def get_group_sources(device, groups_sources, update):
    if (not device["groupId"] in groups_sources) or update:
        req = requests.get(url = f"{build_ip_control_url(device)}/groups/current/sources")
        groups_sources[device["groupId"]] = req.json()
    return groups_sources[device["groupId"]]

def get_group_current_source(device, groups_current_source, update):
    if (not device["groupId"] in groups_current_source) or update:
        req = requests.get(url = f"{build_ip_control_url(device)}/groups/current/sources/current")
        groups_current_source[device["groupId"]] = req.json()
    return groups_current_source[device["groupId"]]

def set_group_playback_state(device, source_id, state):
    requests.post(url = f"{build_ip_control_url(device)}/groups/current/sources/{source_id}/playback/{state}")

def refresh_dicts(devices, systems, systems_volume, groups_sources, groups_current_source, rescan):
    skip_devices = False
    if not len(devices) or rescan:
        skip_devices = True
        devices.clear()
        zeroconf_devices = list_zeroconf_devices()
        for device_cache in zeroconf_devices:
            device_data = {"ip": device_cache.parsed_addresses()[0], "port": device_cache.port, "path": device_cache.properties[b"path"].decode("utf-8")}
            get_device(device_data, devices, True)
        
    for device in devices:
        if not skip_devices:
            get_device(devices[device], devices, True)
        if systems is not None:
            get_system(devices[device], systems, True)
        if systems_volume is not None:
            get_system_volume(devices[device], systems_volume, True)
        if groups_sources is not None:
            get_group_sources(devices[device], groups_sources, True)
        if groups_current_source is not None:
            get_group_current_source(devices[device], groups_current_source, True)