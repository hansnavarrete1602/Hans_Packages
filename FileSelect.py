from tkinter import filedialog
import os


def select_file():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select a File",
                                          filetypes=(("all files",
                                                      "*.*"),
                                                     ("Text files",
                                                      "*.txt*"),
                                                     ("Excel files",
                                                      "*.xlsx*"),
                                                     ("CSV files",
                                                      "*.csv*"),
                                                     ("PDF files",
                                                      "*.pdf*"),
                                                     ("PNG files",
                                                      "*.png*"),
                                                     ("JPG files",
                                                      "*.jpg*")))
    return filename
