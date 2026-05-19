import customtkinter as ctk
from ui.main_screen import MainScreen

def main():
    ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
    ctk.set_default_color_theme("green")  # Default color theme

    app = MainScreen()
    app.mainloop()

if __name__ == "__main__":
    main()
