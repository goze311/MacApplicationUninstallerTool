import tkinter as tk
from tkinter import filedialog, messagebox
from main.service.impl.duplicate_file_logic import DuplicateFileLogic


class DuplicateFileFinderUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Duplicate File Finder")
        self.geometry("600x400")

        self.path_entry = tk.Entry(self, width=50)
        self.check_button = tk.Button(self, text="Check Now", state="disabled", command=self.check_duplicates)

        # Other UI components...

        self.path_entry.pack()
        self.check_button.pack()

        # Other UI components packing...

    def select_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)
            self.check_button.config(state="normal")

    def check_duplicates(self):
        path = self.path_entry.get()
        if path:
            logic = DuplicateFileLogic(path)
            logic.check_for_duplicates()
        else:
            messagebox.showinfo("Error", "Please select a file path.")


if __name__ == "__main__":
    app = DuplicateFileFinderUI()
    app.mainloop()
