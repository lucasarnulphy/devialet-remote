import typer
import dos2
import list
from config import *

app = typer.Typer()

@app.callback()
def device_init():
    if config_devialet_device_id in devices_dict: return

    if config_devialet_ip:
        devices_dict[config_devialet_device_id] = {"deviceId": config_devialet_device_id, "systemId": "", "groupId": "", "ip": config_devialet_ip, "port": config_devialet_port, "path": config_devialet_path}
    else:
        dos2.refresh_dicts(devices_dict, None, None, None, None, False)

@app.command()
def volume_get():
    if config_devialet_device_id in devices_dict:
        volume = dos2.get_system_volume(devices_dict[config_devialet_device_id], systems_volume_dict, True)
        print(f"Volume: {volume['systemVolume']}")
        return volume['systemVolume']

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return None

@app.command()
def volume_set(volume: int):
    if config_devialet_device_id in devices_dict:
        dos2.set_system_volume(devices_dict[config_devialet_device_id], volume)
        print(f"Volume changed: {volume}")
        return True

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return False

@app.command()
def volume_up():
    volume = volume_get()

    if volume is not None:
        volume += 1
        return volume_set(min([volume, 100]))

    return False

@app.command()
def volume_down():
    volume = volume_get()

    if volume is not None:
        volume -= 1
        return volume_set(max([volume, 0]))

    return False

@app.command()
def source_get():
    if config_devialet_device_id in devices_dict:
        source = dos2.get_group_current_source(devices_dict[config_devialet_device_id], groups_current_source_dict, True)
        list.display_sources([source['source']],"")
        return source['source']

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return None

@app.command()
def play():
    if config_devialet_device_id in devices_dict:
        dos2.set_group_playback_state(devices_dict[config_devialet_device_id], config_devialet_source_id, "play")
        print(f"Playing source: {config_devialet_source_id}")
        return True

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return False

@app.command()
def pause():
    if config_devialet_device_id in devices_dict:
        dos2.set_group_playback_state(devices_dict[config_devialet_device_id], config_devialet_source_id, "pause")
        print(f"Paused source: {config_devialet_source_id}")
        return True

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return False

@app.command()
def mute():
    if config_devialet_device_id in devices_dict:
        dos2.set_group_playback_state(devices_dict[config_devialet_device_id], config_devialet_source_id, "mute")
        print(f"Muted source: {config_devialet_source_id}")
        return True

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return False

@app.command()
def unmute():
    if config_devialet_device_id in devices_dict:
        dos2.set_group_playback_state(devices_dict[config_devialet_device_id], config_devialet_source_id, "unmute")
        print(f"Unmuted source: {config_devialet_source_id}")
        return True

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return False

@app.command()
def mute_toggle():
    if config_devialet_device_id in devices_dict:
        is_muted = muted()
        if is_muted is None:
            return False
        if is_muted:
            return unmute()
        else:
            return mute()

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return False

@app.command()
def paused():
    if config_devialet_device_id in devices_dict:
        source = dos2.get_group_current_source(devices_dict[config_devialet_device_id], groups_current_source_dict, True)
        paused_bool = (source['playingState'] == "paused")
        print(f"Paused: {paused_bool}")
        return paused_bool

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return None

@app.command()
def muted():
    if config_devialet_device_id in devices_dict:
        source = dos2.get_group_current_source(devices_dict[config_devialet_device_id], groups_current_source_dict, True)
        muted_bool = (source['muteState'] == "muted")
        print(f"Muted: {muted_bool}")
        return muted_bool

    print(f"Error: Could not find the given config_devialet_device_id ({config_devialet_device_id})")
    return None