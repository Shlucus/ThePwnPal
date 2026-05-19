import customtkinter as ctk
from core.controller import Controller
from ui.scan_result_screen import ScanResultScreen
import requests

class MainScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PwnPal Tool")

        # Set the window to fullscreen
        self.wm_attributes("-fullscreen", True)
        self.config(cursor="none") # removes cursor
        self.controller = Controller()

        self.label = ctk.CTkLabel(self, text="Select Scan Type", font=("Arial", 24))  # Increase font size
        self.label.pack(pady=20)

        self.scan_type = ctk.StringVar(value="Access Point Scan")
        self.option_menu = ctk.CTkOptionMenu(self, values=["Access Point Scan", "Handshake Sniffing", "Webhook Request"], variable=self.scan_type, font=("Arial", 18), width=200, height=50)  # Increase font size and set size
        self.option_menu.pack(pady=10)

        self.start_button = ctk.CTkButton(self, text="Start Scan", command=self.start_scan, font=("Arial", 18), width=200, height=50)  # Increase font size and button size
        self.start_button.pack(pady=20)

        # Add exit button
        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.exit_application, font=("Arial", 18), width=200, height=50)  # Increase font size and button size
        self.exit_button.pack(pady=20)

    def start_scan(self):
        scan_type = self.scan_type.get()
        if scan_type == "Webhook Request":
            results = self.perform_webhook_request()
        else:
            results = self.controller.perform_scan(scan_type)
        self.show_results(scan_type, results)

    def perform_webhook_request(self):
        url = "https://webhook.site/token/3eafda79-5636-4006-a51c-eb1a112c928b/request/latest/raw"  # Replace with your webhook URL
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to reach webhook: {response.status_code}"

    def show_results(self, scan_type, results):
        self.withdraw()  # Hide the main screen
        ScanResultScreen(self, scan_type, results).mainloop()

    def exit_application(self):
        self.destroy()
