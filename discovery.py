from time import sleep
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
from rich.progress import track
from config import *

class ZeroconfListener(ServiceListener):
    cache = []

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        pass

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        if not info.properties:
            return
        if not info.properties.get(b"manufacturer",b"").decode("utf-8")  == "Devialet":
            return
        if not info.properties.get(b"ipControlVersion",b"").decode("utf-8")  == "1":
            return
        if not b"path" in info.properties:
            return
        if not len(info.parsed_addresses()):
            return
        self.cache.append(info)

def list_zeroconf_devices():
    zeroconf = Zeroconf()
    listener = ZeroconfListener()
    ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
    sleep_duration = config_discovery_scan_duration  / 100

    for value in track(range(100), description="Searching devices..."):
        sleep(sleep_duration)

    zeroconf.close()
    return listener.cache