import pywifi
import time

def list_all_interfaces():
    wifi = pywifi.PyWiFi()
    interfaces = wifi.interfaces()

    if not interfaces:
        print("No wireless interfaces found.")
        return

    # Use the 3rd wireless interface ('wlan1' on the PwnPal)
    iface = interfaces[len(interfaces) - 1]

    print(f"Scanning for Wi-Fi networks using interface: {iface.name()}")

    # Start scanning
    iface.scan()
    time.sleep(3)  # Wait for the scan to complete

    # Fetch scan results
    results = iface.scan_results()

    if not results:
        print("No networks found.")
        return

    myList = []

    print("\nNearby Wi-Fi Networks:")
    for idx, network in enumerate(results):
        ssid = network.ssid if network.ssid else "Hidden SSID"
        band = "2.4 GHz" if network.freq < 3000 else "5 GHz"

        myList.append(f"SSID: {ssid}, Band: {band}")
        print(f"{idx + 1}. SSID: {ssid}, Band: {band}")
    return myList









#
# def get_wifi_security(auth, cipher):
#     auth_types = {
#         const.AUTH_ALG_OPEN: "Open",
#         const.AUTH_ALG_SHARED: "Shared",
#     }
#     cipher_types = {
#         const.CIPHER_TYPE_NONE: "None",
#         const.CIPHER_TYPE_WEP: "WEP",
#         const.CIPHER_TYPE_TKIP: "TKIP",
#         const.CIPHER_TYPE_CCMP: "CCMP (AES)",
#     }
#
#     auth_name = auth_types.get(auth, "Unknown")
#     cipher_name = cipher_types.get(cipher, "Unknown")
#     return f"{auth_name}, {cipher_name}"
#
# def scan_wifi():
#     wifi = pywifi.PyWiFi()
#     iface = wifi.interfaces()[0]  # Get the first wireless interface
#
#     iface.scan()  # Start scanning for networks
#     time.sleep(2)  # Wait for the scan to complete
#
#     scan_results = iface.scan_results()
#
#     for network in scan_results:
#         security = get_wifi_security(network.auth, network.akm)
#         band = "2.4 GHz" if network.freq < 3000 else "5 GHz"
#         print(f"SSID: {network.ssid}, Signal: {network.signal}, Band: {band}, Security: {security}")
#
