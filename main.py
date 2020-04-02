import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class MainClass(tk.Tk):
    def __init__(self, Root, *args, **kwargs):
        self.Root = Root
        self.Root.title('Getit')
        self.Root.geometry('500x500')

def Main():
    Root = tk.Tk()
    Getit = MainClass(Root)
    Root.mainloop()

if __name__ == '__main__':
    Main()