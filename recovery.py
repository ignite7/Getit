""" All libraries and modules imported """

# Tkinter libraries
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

# System info
import platform
import sys


# Sqlite3 library
import sqlite3


class RecoveryClass(tk.Tk):
    """ Class url recovery manager """
    
    def __init__(self, Root, Url, Types, Rename, Path, Lyrics):
        """ Main initial method of url recovery """
        
        # Assignament variables
        self._root = Root
        
        self._main_window = tk.Toplevel(self._root)
        self._main_window.title('URL Recovery')
        self._main_window.geometry('600x610')
        self._main_window.resizable(False, False)
        
        
        # ICO image for windows
        if sys.platform.startswith('win'):
            self._root.iconbitmap('.\\img\\icon.ico')
            
            
        # Constants variables
        _URL = Url
        _TYPES = Types 
        _RENAME = Rename
        _PATH_DIR = Path
        _LYRICS = Lyrics
        
        
        # Canvas, frame and scroll bar
        _scroll = tk.Scrollbar(self._main_window)
        self._canvas = tk.Canvas(self._main_window, yscrollcommand = _scroll.set)
        
        _scroll.config(command = self._canvas.yview)
        _scroll.pack(side = 'right', fill = 'y')
        
        self._frame = tk.Frame(self._canvas)
        self._canvas.create_window(0, 0, window = self._frame, anchor = 'nw')
        
        
        # Constants functions
        def _update_window(self):
            """ Private function managet to update the window 
            of the program.
            """
            
            self._main_window.update()
            self._canvas.config(scrollregion = self._canvas.bbox('all'))
            self._canvas.pack()
            self._frame.pack()
         
         
        # Short part of code of the logo
        def _url_recovery_complement():
            """ Private function manager to complement the 
            manual image.
            """
            
            recovery_label = tk.Label(self._frame, image = recovery)
            recovery_label.image = recovery # Reference
            recovery_label.grid(row = 0, columnspan = 1, column = 0, sticky = 'nswe', pady = 20)
         
            
        # Image
        if sys.platform.startswith('linux'):
            recovery = ImageTk.PhotoImage(Image.open('./img/url_recovery.png'))
            _url_recovery_complement()
            
        else:
            recovery = ImageTk.PhotoImage(Image.open('.\\img\\url_recovery.png'))
            _url_recovery_complement() 
        
        
        connect_db = sqlite3.connect('./url_recovery.sqlite3')
        cursor_db = connect_db.cursor()
        
        try:
            cursor_db.execute('SELECT * FROM backups WHERE id >= 3')
            print_db = cursor_db.fetchall()
        
        finally:
            connect_db.commit()
            connect_db.close() # Connection closed

        for dates in print_db:
            self.re_label = tk.Label(self._frame, text = f'{dates[:]}', font = _LYRICS[1], fg = 'red')
            self.re_label.grid(row = 1, column = 0, sticky = 'e', padx = 5)
        
        _update_window(self) # Update window    