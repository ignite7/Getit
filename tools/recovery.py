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


# Modules
from .wrappers.decorate import DecorateClass as Decorate


class RecoveryClass(tk.Tk):
    """ Class url recovery manager """
    
    def __init__(self, Root, Url, Types, Rename, Path, Lyrics, Mkdir, History):
        """ Main initial method of url recovery """
        
        # Assignament variables
        self._root = Root
        
        
        # ICO image for windows
        if sys.platform.startswith('win32'):
            self._root.iconbitmap('.\\img\\icon.ico')
        
        # Check data base exists
        if os.path.exists('./data_base/url_recovery.sqlite3'):

            # Assignament of a new 'root'
            self._main_window = tk.Toplevel(self._root)
            self._main_window.title('URL Recovery')
            self._main_window.geometry('600x650')
            self._main_window.resizable(False, False)
        
        
            # Constants variables
            self.URL = Url
            self.TYPES = Types 
            self.RENAME = Rename
            self.PATH_DIR = Path
            self.LYRICS = Lyrics
            self.UID = tk.IntVar() # Get id
            self.MKDIR = Mkdir
            self.HISTORY = History
        
        
            # Canvas, frame and scroll bar
            self._canvas = tk.Canvas(self._main_window)
            self._frame = tk.Frame(self._canvas)
        
            
            # Image
            if sys.platform.startswith('linux'):
                self.recovery = ImageTk.PhotoImage(Image.open('./img/url_recovery.png'))
                self._logo_complement()
            
            else:
                self.recovery = ImageTk.PhotoImage(Image.open('.\\img\\url_recovery.png'))
                self._logo_complement()
            
            
            # Show the dates and update window
            self._fetch_db()
            self._update_window()
                
        else:
            error_not_exists = messagebox.showinfo(
                parent = self._root,
                title = 'There Is Not Downloads Yet',
                message = 'There still isn\'t downloads that can show to you.' 
            )


    def _update_window(self):
        """ Private function managet to update the window 
        of the program.
        """
            
        self._main_window.update()
        self._canvas.pack()
        self._frame.pack()
        
        
    def _logo_complement(self):
        """ Private function manager to complement the 
        manual image.
        """
        
        self.recovery_label = tk.Label(self._frame, image = self.recovery)
        self.recovery_label.image = self.recovery # Reference
        self.recovery_label.grid(row = 0, columnspan = 4, column = 0, sticky = 'nswe', pady = 10)
   
        
    @Decorate._connection_db
    def _fetch_db(self):
        """ Private function manager of show the
        dates of the data base in screen.
        """
            
        self.cursor_db.execute('SELECT id, url, type, rename, path FROM backups')
        self.print_db = self.cursor_db.fetchall()
                
                
        # Introduction
        introduction = tk.Label(self._frame, text = 'Recover your old downloads in one click!', font = self.LYRICS[0])
        introduction.grid(row = 1, columnspan = 4, sticky = 'we', pady = 10)
                
                
        # ListBox creation, vertical and horizontal scrollbar
        v_scrollbar = tk.Scrollbar(self._frame, orient = 'vertical')
        v_scrollbar.grid(row = 2, column = 4, sticky = 'ns')
        h_scrollbar = tk.Scrollbar(self._frame, orient = 'horizontal')
        h_scrollbar.grid(row = 3, columnspan = 4, sticky = 'we')
                
        self.fetch = tk.Listbox(self._frame, width = 60, height = 20, cursor = 'hand2', font = self.LYRICS[1])
        self.fetch.config(xscrollcommand = h_scrollbar.set, yscrollcommand = v_scrollbar.set)
        self.fetch.config(selectmode = tk.BROWSE, borderwidth = 2)
        self.fetch.grid(row = 2, columnspan = 4, sticky = 'we')
                
        v_scrollbar.config(command = self.fetch.yview)
        h_scrollbar.config(command = self.fetch.xview)
                
                   
        # Show the dates inside of listbox
        space = ' ' * 7
        self.fetch.insert(tk.END, f'[ID]{space}[URL]{space}[TYPE]{space}[RENAME]{space}[PATH]')
                
        dates = [date[:] for date in self.print_db]
        for idx, items in enumerate(dates):
            self.fetch.insert(idx + 1, f'{items}')
                
                
        # Uid field    
        label_uid = tk.Label(self._frame, text = 'Insert ID:', font = self.LYRICS[2])
        label_uid.grid(row = 4, column = 0, sticky = 'e', padx = 5, pady = 20)
                
                
        self.UID.set(1) # Set '1' by default
        insert_uid = tk.Entry(self._frame, font = self.LYRICS[1], width = 5, textvariable = self.UID)
        insert_uid.grid(row = 4, column = 1, sticky = 'w', padx = 5, pady = 20)
                
                
        # Get uid button
        button_uid = tk.Button(self._frame, text = 'Row Copy', command = lambda: self._get_uid())
        button_uid.config(relief = 'groove', borderwidth = 2, cursor = 'hand2', font = self.LYRICS[1])
        button_uid.grid(row = 4, column = 2, sticky = 'w', padx = 5, pady = 20)
                
                
        # Delete uid button
        delete_uid = tk.Button(self._frame, text = 'Row Delete', command = lambda: self._delete_uid())
        delete_uid.config(relief = 'groove', borderwidth = 2, cursor = 'hand2', font = self.LYRICS[1], fg = 'red')
        delete_uid.grid(row = 4, column = 3, sticky = 'w', padx = 5, pady = 20)

            
    @Decorate._connection_db  
    def _get_uid(self):
        """ Private function manager to put the 
        data again in the fields.
        """
                
        self.cursor_db.execute(f'SELECT url, type, rename, path, track, folder FROM backups WHERE id = {str(self.UID.get())}')
        self.print_db = self.cursor_db.fetchall()
                
        get_message = tk.Label(self._frame, text = f'ID: {str(self.UID.get())} has been copied!')
        get_message.config(font = self.LYRICS[1], fg = 'red')
        get_message.grid(row = 5, columnspan = 4, sticky = 'we')
                
            
        # Puts the info in the main window
        for dates in self.print_db:
            self.URL.set(dates[0])
            self.TYPES.set(dates[1])
            self.RENAME.set(dates[2])
            self.PATH_DIR = f'{dates[3]}'
            self.HISTORY.set(dates[4])
            self.MKDIR.set(dates[5])
            

        get_message.after(1000, get_message.destroy) # Destroy after 1 seconds
        self.UID.set('1') # Clean
            
            
    @Decorate._connection_db
    def _delete_uid(self):
        """ Private funtion manager to delete
        the dates from the data base.
        """
                
        self.cursor_db.execute(f'DELETE FROM backups WHERE id = {str(self.UID.get())}')
                
        delete_message = tk.Label(self._frame, text = f'ID: {str(self.UID.get())} has been deleted!')
        delete_message.config(font = self.LYRICS[1], fg = 'red')
        delete_message.grid(row = 5, columnspan = 4, sticky = 'we')
                
        delete_message.after(1000, delete_message.destroy) # Destroy after 1 seconds
        self.UID.set('1') # Clean 