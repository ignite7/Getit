""" All libraries and modules imported """

# Tkinter libraries
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

# System info
import platform
import sys
import os


# Sqlite3 library
import sqlite3


class RecoveryClass(tk.Tk):
    """ Class url recovery manager """
    
    def __init__(self, Root, Url, Types, Rename, Path, Lyrics):
        """ Main initial method of url recovery """
        
        # Assignament variables
        self._root = Root
        
        
        # Check data base exists
        if os.path.exists('./url_recovery.sqlite3'):
            
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
         
        
            # Data base connection
            def _connection_db(function):
                """ Decorate function manager to implement
                the connection with the data base.
                """
            
                def wrapper(self):
                    self.connect_db = sqlite3.connect('./url_recovery.sqlite3')
                    self.cursor_db = self.connect_db.cursor()
                
                    function(self)
                
                    self.connect_db.commit()
                    self.connect_db.close()
                
                return wrapper
        
        
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
          
        
            @_connection_db
            def _fetch_db(self):
                """ Private function manager of show the
                dates of the data base in screen.
                """
            
                self.cursor_db.execute('SELECT * FROM backups WHERE id >= 3')
                print_db = self.cursor_db.fetchall()
            
                for dates in print_db:
                    self.re_label = tk.Label(self._frame, text = f'{dates[:]}', font = _LYRICS[1])
                    self.re_label.grid(row = 1, column = 0, sticky = 'e', padx = 5)
        
        
            _fetch_db(self) # Call function
            _update_window(self) # Update window
        
        else:
            error_not_exists = messagebox.showinfo(
                parent = self._root,
                title = 'There Is Not Downloads Yet',
                message = 'There still isn\'t downloads that can show to you.' 
            )