import tkinter as tk
from tkinter import filedialog

def drag_and_drop_file():
    """Opens a file dialog to allow drag-and-drop file selection."""
    # Create a Tkinter root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All files", "*.*")])

    if file_path:
        print(f"File selected: {file_path}")
    else:
        print("No file selected.")

if __name__ == "__main__":
    drag_and_drop_file()
