"""
VTEX Freight Converter
Autor: Taís Zimmer + ChatGPT

Arquivo principal da aplicação.
"""

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox


class MainWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VTEX Freight Converter")
        self.root.geometry("900x550")
        self.root.minsize(900, 550)
        self.selected_file = ""
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="VTEX Freight Converter",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=20)

        frame = tk.Frame(self.root)
        frame.pack(fill="x", padx=20)

        tk.Label(frame, text="Arquivo:").grid(row=0, column=0, sticky="w")

        self.file_entry = tk.Entry(frame, width=90)
        self.file_entry.grid(row=1, column=0, padx=(0, 10), pady=5)

        browse = tk.Button(frame, text="Selecionar...", command=self.select_file)
        browse.grid(row=1, column=1)

        self.info = tk.Label(
            self.root,
            text="Nenhum arquivo selecionado.",
            anchor="w",
            justify="left"
        )
        self.info.pack(fill="x", padx=20, pady=15)

        buttons = tk.Frame(self.root)
        buttons.pack()

        self.preview_button = tk.Button(
            buttons,
            text="Visualizar",
            width=20,
            state="disabled",
            command=self.preview
        )
        self.preview_button.grid(row=0, column=0, padx=10)

        self.convert_button = tk.Button(
            buttons,
            text="Converter",
            width=20,
            state="disabled",
            command=self.convert
        )
        self.convert_button.grid(row=0, column=1, padx=10)

        self.status = tk.Label(
            self.root,
            text="Pronto.",
            fg="blue",
            anchor="w"
        )
        self.status.pack(fill="x", side="bottom", padx=20, pady=10)

    def select_file(self):
        filename = filedialog.askopenfilename(
            title="Selecionar planilha",
            filetypes=[
                ("Excel", "*.xlsx *.xls"),
                ("Todos", "*.*")
            ]
        )

        if not filename:
            return

        self.selected_file = filename
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, filename)

        file = Path(filename)
        self.info.config(
            text=f"""
Arquivo: {file.name}

Local: {file.parent}
"""
        )

        self.preview_button.config(state="normal")
        self.convert_button.config(state="normal")
        self.status.config(text="Arquivo carregado.")

    def preview(self):
        messagebox.showinfo(
            "Visualizar",
            "Na próxima versão será exibida a pré-visualização da planilha."
        )

    def convert(self):
        messagebox.showinfo(
            "Conversão",
            "Conversor será implementado na próxima etapa."
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()
