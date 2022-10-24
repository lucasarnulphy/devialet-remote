from pynput.keyboard import Key

config_discovery_scan_duration = 1

# DeviceId-based configuration
config_devialet_device_id = ""

# IP-based configuration
config_devialet_ip = ""
config_devialet_port = 80
config_devialet_path = "/ipcontrol/v1"

# SourceId configuration
config_devialet_source_id = "current"

# Listener configuration
config_listener_dict = {}
config_listener_dict[Key.f1] = "action.volume_down()"
config_listener_dict[Key.f2] = "action.volume_up()"
config_listener_dict[Key.f3] = "action.play() and action.mute_toggle()"

# Shared dicts, do not edit this part
devices_dict = dict()
systems_dict = dict()
systems_volume_dict = dict()
groups_sources = dict()
groups_current_source_dict = dict()