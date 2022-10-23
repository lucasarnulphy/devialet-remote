import typer
import dos2
from config import *

app = typer.Typer()

def display_device(device, indent):
        print(f"{indent}- Device: {device['deviceName']} - {device['role']} ({device['model']})")
        print(f"{indent}  IP Control URL: {dos2.build_ip_control_url(device)}")
        print(f"{indent}  Serial: {device['serial']}")
        print(f"{indent}  DeviceId: {device['deviceId']}")
        print(f"{indent}  SystemId: {device['systemId']}")
        print(f"{indent}  GroupId: {device['groupId']}")

@app.command()
def devices():
    dos2.refresh_dicts(devices_dict, None, None, None, None, False)
    first = True
    for device in devices_dict:
        display_device(devices_dict[device], "")

@app.command()
def systems():
    dos2.refresh_dicts(devices_dict, systems_dict, None, None, None, False)
    first = True
    for system in systems_dict:
        system_value = systems_dict[system]
        print(f"- System: {system_value['systemName']}")
        print(f"  SystemId: {system_value['systemId']}")
        print(f"  GroupId: {system_value['groupId']}")
        for device in devices_dict:
            device_value = devices_dict[device]
            if device_value["systemId"] == system: 
                display_device(device_value, "  ")

def display_sources(source, indent):
    for source_value in source:
        print(f"{indent}- Type: {source_value['type']}")
        print(f"{indent}  SourceId: {source_value['sourceId']}")
        print(f"{indent}  DeviceId: {source_value['deviceId']}")

@app.command()
def sources():
    dos2.refresh_dicts(devices_dict, None, None, groups_sources, None, False)
    first = True
    for device in devices_dict:
        display_device(devices_dict[device], "")
        device_value = devices_dict[device]
        groups_sources_value = groups_sources[device_value["groupId"]]
        display_sources(groups_sources_value["sources"], "  ")