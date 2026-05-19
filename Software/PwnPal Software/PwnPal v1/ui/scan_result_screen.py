import customtkinter as ctk
from core.utils import format_scan_results

class ScanResultScreen(ctk.CTkToplevel):
    def __init__(self, parent, scan_type, results):
        super().__init__()
        self.title(f"{scan_type} Results")

        # Set the window to fullscreen
        self.wm_attributes("-fullscreen", True)

        self.results_label = ctk.CTkLabel(self, text="Scan Results", font=("Arial", 16))
        self.results_label.pack(pady=10)

        formatted_results = format_scan_results(results) if isinstance(results, list) else str(results)
        self.textbox = ctk.CTkTextbox(self, height=400, width=350)
        self.textbox.insert("1.0", formatted_results)
        self.textbox.configure(state="disabled")
        self.textbox.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.close, font=("Arial", 18), width=200, height=50)  # Increase font size and button size
        self.back_button.pack(pady=10)

        self.parent = parent

    def close(self):
        self.destroy()
        self.parent.deiconify()  # Show the main screen
