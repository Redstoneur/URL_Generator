import argparse
import tkinter as tk
from urllib.parse import quote

import pyperclip


class URLConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("URL Converter")

        self.label = tk.Label(self, text="Entrez l'URL:")
        self.label.pack()

        self.url_entry = tk.Entry(self, width=40)
        self.url_entry.pack()

        self.convert_button = tk.Button(self, text="Convertir", command=self.convert_url)
        self.convert_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        self.copy_button = tk.Button(self, text="Copier", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def convert_url(self):
        entered_url = self.url_entry.get()

        try:
            # Convertir l'URL en langage standard
            converted_url = quote(entered_url, safe=':/?=&')

            # Afficher le résultat
            self.result_label.config(text=f"URL convertie: {converted_url}")
        except Exception as e:
            self.result_label.config(text=f"Erreur: {str(e)}")

    def copy_to_clipboard(self):
        converted_url = self.result_label.cget("text").split(": ", 1)[1]  # Extraire l'URL du texte

        # Copier l'URL dans le presse-papiers
        pyperclip.copy(converted_url)


def run_gui():
    root = URLConverterApp()
    root.mainloop()


def run_command_line(url_str: str):
    try:
        converted_url = quote(url_str, safe=':/?=&')
        print(f"URL convertie: {converted_url}")
        pyperclip.copy(converted_url)
    except Exception as e:
        print(f"Erreur: {str(e)}")


if __name__ == "__main__":
    program_name = "URL Generator"
    program_version = "v1.0.1"
    program_description = "Convertir une URL en langage standard"

    parser = argparse.ArgumentParser(description=f"{program_name} : {program_description}")
    parser.add_argument("-c", "--cli", help="Run in Command Line Mode", action="store_true")
    parser.add_argument("-u", "--url", help="URL to convert (Command Line Mode Only)", default=None)
    parser.add_argument("-v", "--version", action="version", version=f"{program_name} [%(prog)s] : {program_version}")

    args = parser.parse_args()

    if args.cli:
        url: str = args.url
        while url is None:
            url = input("URL à convertir: ")
        run_command_line(url)
    else:
        run_gui()
