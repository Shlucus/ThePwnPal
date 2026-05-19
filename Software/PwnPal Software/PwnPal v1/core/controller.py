from core.scanner import Scanner

class Controller:
    def __init__(self):
        self.scanner = Scanner()

    def perform_scan(self, scan_type):
        if scan_type == "Access Point Scan":
            return self.scanner.scan_access_points()
        elif scan_type == "Handshake Sniffing":
            return self.scanner.sniff_handshake()
        else:
            raise ValueError(f"Unknown scan type: {scan_type}")
