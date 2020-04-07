""" All libraries and modules imported """

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class DownloadClass(tk.Tk):
    """ Class download manager """
    
    def __init__(self, Root, Frame, Lyrics):
        """ Main initial method of download """
        
        # Assignament variables
        self._root = Root
        self._frame = Frame
        
        # Assignament lyrics
        _LYRICS = Lyrics
        
        test = tk.Label(self._frame, text = 'Hola', font = _LYRICS[1])
        test.grid(row = 6, columnspan = 2)