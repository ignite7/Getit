import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class MainClass(tk.Tk):
    def __init__(self, Root, *args, **kwargs):
        self._root = Root
        self._root.title('Getit')
        self._root.geometry('500x500')

def Main():
    root = tk.Tk()
    getit = MainClass(root)
    root.mainloop()

if __name__ == '__main__':
    Main()