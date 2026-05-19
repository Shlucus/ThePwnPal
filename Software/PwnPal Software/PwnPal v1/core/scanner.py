from core.Scans.get_access_points import list_all_interfaces


class Scanner:
    def scan_access_points(self):
        # Simulated scan results

        interfaces = list_all_interfaces()

        for idx,interface in enumerate(interfaces):
            print(idx)
        # return interfaces

        return interfaces

        # myList = []
        #
        # for idx,interface in enumerate(interfaces):
        #     myList.append({f"{idx + 1}. SSID: {interface.ssid}, Band: {interface.band}"})
        #     myList.append("goon")


        # return [
        #     {"SSID": "Network1", "Security": "WPA2", "Frequency": "2.4 GHz"},
        #     {"SSID": "Network2", "Security": "Open", "Frequency": "5 GHz"},
        # ]



    def sniff_handshake(self):
        # Simulated handshake sniffing result
        return {"status": "Success", "message": "Handshake captured."}
