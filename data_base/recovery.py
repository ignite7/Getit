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
        if os.path.exists('./data_base/url_recovery.sqlite3'):
            
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
            self._PATH_DIR = Path
            _LYRICS = Lyrics
            _UID = tk.StringVar() # Get id
        
        
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
                    self.connect_db = sqlite3.connect('./data_base/url_recovery.sqlite3')
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
                recovery_label.grid(row = 0, columnspan = 4, column = 0, sticky = 'nswe', pady = 20)
         
            
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
            
                self.cursor_db.execute('SELECT id, url, type FROM backups')
                self.print_db = self.cursor_db.fetchall()
                
                
                # ListBox creation
                self.fetch = tk.Listbox(self._frame, width = 60, height = 20, cursor = 'hand2', font = _LYRICS[1])
                self.fetch.grid(row = 1, columnspan = 4, sticky = 'we')
                
                space = ' ' * 15
                self.fetch.insert(tk.END, f'ID{space}URL{space}TYPE') # Titles
                
                
                # Show the dates inside of listbox
                dates = [date[:] for date in self.print_db]
                for idx, items in enumerate(dates):
                    self.fetch.insert(idx + 1, items)
                
                
                # Uid field    
                label_uid = tk.Label(self._frame, text = 'Insert ID:', font = _LYRICS[1])
                label_uid.grid(row = 2, column = 0, sticky = 'e', padx = 5, pady = 20)
                
                _UID.set('1') # Set '1' by default
                insert_uid = tk.Entry(self._frame, font = _LYRICS[1], width = 5, textvariable = _UID)
                insert_uid.grid(row = 2, column = 1, sticky = 'w', padx = 5, pady = 20)
                
                
                # Get uid button
                button_uid = tk.Button(self._frame, text = 'Row Copy', command = lambda: _get_uid(self))
                button_uid.config(relief = 'groove', borderwidth = 2, cursor = 'hand2', font = _LYRICS[1])
                button_uid.grid(row = 2, column = 2, sticky = 'w', padx = 5, pady = 20)
                
                
                # Delete uid button
                delete_uid = tk.Button(self._frame, text = 'Row Delete', command = lambda: _delete_uid(self))
                delete_uid.config(relief = 'groove', borderwidth = 2, cursor = 'hand2', font = _LYRICS[1], fg = 'red')
                delete_uid.grid(row = 2, column = 3, sticky = 'w', padx = 5, pady = 20)
                
            
            @_connection_db    
            def _get_uid(self):
                """ Private function manager to put the 
                data again in the fields.
                """
                
                self.cursor_db.execute(f'SELECT url, type, rename, path FROM backups WHERE id = {_UID.get()}')
                self.print_db = self.cursor_db.fetchall()
                
                
                # Puts the info in the main window
                for dates in self.print_db:
                    _URL.set(dates[0])
                    _TYPES.set(dates[1])
                    _RENAME.set(dates[2])
                    self._PATH_DIR = f'{dates[3]}' # Break
            
            
            @_connection_db
            def _delete_uid(self):
                """ Private funtion manager to delete
                the dates from the data base.
                """
                
                self.fetch.delete(_UID.get())
                self.cursor_db.execute(f'DELETE FROM backups WHERE id = {_UID.get()}')
                
                
            _fetch_db(self) # Call function
            _update_window(self) # Update window
        
        else:
            error_not_exists = messagebox.showinfo(
                parent = self._root,
                title = 'There Is Not Downloads Yet',
                message = 'There still isn\'t downloads that can show to you.' 
            )