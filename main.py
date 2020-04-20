""" All libraries and modules imported """

# Tkinter 
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


# System info
import getpass
import platform
import sys


# Modules
from tools.menu import MenuClass as Menu
from tools.download import DownloadClass as Download
from tools.recovery import RecoveryClass as Recovery
from data_base.connection_db import ConnectionClass as DataBase


class MainClass(tk.Tk):
    """ Main Class of the window, and executor of
    another variables
    """
    
    def __init__(self, Root, *args, **kwargs):
        """ Method of init when the program starts """  
            
        # Assignament variables
        self._root = Root
        self._root.title('Getit')
        self._root.geometry('600x650')
        self._root.resizable(False, False)
        
        
        # ICO image for windows
        if sys.platform.startswith('win32'):
            self._root.iconbitmap('.\\img\\icon.ico')
        
        
        # Constants variables inserts
        self.URL = tk.StringVar()
        self.TYPES = tk.StringVar()
        self.RENAME = tk.StringVar()
        self.USER = getpass.getuser() # Get the user name
        self.MKDIR = tk.BooleanVar()
        self.HISTORY = tk.BooleanVar()
        
        if sys.platform.startswith('linux'): 
            self.PATH_DIR = f'/home/{self.USER}'
        
        else:
            self.PATH_DIR = f'C:\\Users\\{self.USER}\\Downloads'
        
        self.LYRICS = (
            ('Courier New', 12, 'bold'),
            ('Courier New', 11, 'normal'),
            ('Courier New', 11, 'italic')
        )
        
        
        # Canvas and frame 
        self._canvas = tk.Canvas(self._root)
        self._frame = tk.Frame(self._canvas)

        
        
        # Image
        if sys.platform.startswith('linux'):
            self.logo = ImageTk.PhotoImage(Image.open('./img/logo.png'))
            self._logo_complement()
            
        else:
            self.logo = ImageTk.PhotoImage(Image.open('.\\img\\logo.png'))
            self._logo_complement()
            
        
        # Introduce cell   
        self.introduce_label = tk.Label(self._frame, text = 'Get anything from URL to your computer!', font = self.LYRICS[0])
        self.introduce_label.grid(row = 1, columnspan = 4, sticky = 'we', pady = 10)
        
        
        # Url cell
        self.url_label = tk.Label(self._frame, text = '* Your URL:', font = self.LYRICS[2])
        self.url_label.grid(row = 2, column = 0, sticky = 'e', padx = 5)
        
        self.url = tk.Entry(self._frame, textvariable = self.URL, font = self.LYRICS[1])
        self.url.grid(row = 2, column = 1, sticky = 'we', pady = 5)
        
        
        # Choose type cell
        self.sort_label =  tk.Label(self._frame, text = '* Choose the type:', font = self.LYRICS[1])
        self.sort_label.grid(row = 3, column = 0, sticky = 'e', padx = 5)
        
        self.TYPES.set('Types')
        list_of_types = ['Anything!', 'Youtube', 'YT Playlist'] # List of types
        
        self.sort = tk.OptionMenu(self._frame, self.TYPES, *list_of_types)
        self.sort.config(font = self.LYRICS[1], relief = 'groove', borderwidth = 2)
        self.sort.grid(row = 3, column = 1, sticky = 'we', pady = 5)
        
        
        # Button that allow continue to the another fields
        self.go_head = tk.Button(self._frame, text = 'Continue', cursor = 'hand2', command = lambda: self._continue())
        self.go_head.config(relief = 'groove', borderwidth = 2, font = self.LYRICS[1])
        self.go_head.grid(row = 4, columnspan = 4, sticky = 'we', pady = 5)
        
        
        # Modules call
        self.recovery = lambda: Recovery(self._root, self.URL, self.TYPES, self.RENAME, self.PATH_DIR, self.LYRICS,
                                         self.MKDIR, self.HISTORY)
        Menu(self._root, self.URL, self.TYPES, self.RENAME, self.PATH_DIR, self.LYRICS, self.recovery, 
             self.MKDIR, self.HISTORY) 
        
        
        # Update and grid of the window
        self._update_window()

        
    def _update_window(self):
        """ Private function managet to update the window 
        of the program.
        """
            
        self._root.update()  
        self._canvas.pack()
        self._frame.pack()
            
            
    def _logo_complement(self):
        """ Private function manager to complement the 
        logo image.
        """
            
        self.logo_label = tk.Label(self._frame, image = self.logo)
        self.logo_label.image = self.logo # Reference
        self.logo_label.grid(row = 0, columnspan = 4, column = 0, sticky = 'nswe', pady = 20)

       
    def _continue(self):
        """ Private function that allow the verification and
        continue of the program (IMPORTANT).
        """
            
        if self.URL.get() == '' or self.TYPES.get() == 'Types':
             self._error_01() # Call error function
            
        else:
            self.go_head.destroy() # Destroy button 'Continue'


            # Check the type
            if self.TYPES.get() == 'Anything!' or self.TYPES.get() == 'Youtube':
                self._rename()
                
                
            # Save the path
            self.save_label = tk.Label(self._frame, text = 'Where do you want save it?', font = self.LYRICS[1])
            self.save_label.grid(row = 6, column = 0, sticky = 'e', padx = 5)
    
            self.save = tk.Button(self._frame, text = 'Open', cursor = 'hand2', command = lambda:self._open_dir())
            self.save.config(relief = 'groove', borderwidth = 2, font = self.LYRICS[1])
            self.save.grid(row = 6, column = 1, sticky = 'we', pady = 5)

            
            # Make dir and make url history
            self.mkdir = tk.Checkbutton(self._frame, text = 'Save in a folder', var = self.MKDIR, font = self.LYRICS[1])
            self.mkdir.grid(row = 7, column = 0, sticky = 'we', padx = 5, pady = 5)
            
            self.history = tk.Checkbutton(self._frame, text = 'Track URL', var = self.HISTORY, font = self.LYRICS[1])
            self.history.grid(row = 7, column = 1, sticky = 'we', padx = 5, pady = 5)
            
            
            # Start button
            self.start = tk.Button(self._frame, text = 'Start Download!', cursor = 'hand2', command = lambda:self._download())
            self.start.config(relief = 'groove', borderwidth = 2, font = self.LYRICS[1])
            self.start.grid(row = 8, column = 0, sticky = 'we', pady = 10)
        
        
            # Button that allow update the type 
            self.go_back = tk.Button(self._frame, text = 'Update The Type', command = lambda:self._update_type())
            self.go_back.config(cursor = 'hand2', relief = 'groove', borderwidth = 2, font = self.LYRICS[1], fg = 'red')
            self.go_back.grid(row = 8, column = 1, sticky = 'we', pady = 10)
        
        
            # Update and grid of the window
            self._update_window()

       
    def _open_dir(self):
        """ Private function manager of establish the path of the dir
        where save the files downloads.
        """
            
        # Check the current OS
        if sys.platform.startswith('linux'):
            self.PATH_DIR = filedialog.askdirectory(
                parent = self._frame, 
                title = 'Choose The Directory', 
                initialdir = '~/'
            )

        else: 
            self.PATH_DIR = filedialog.askdirectory(
                parent = self._frame, 
                title = 'Choose The Directory', 
                initialdir = 'C:\\Downloads'
            )
    
    
    def _rename(self):
        """ Private function that show the field rename if
        the selection is 'URL' or 'Torrent'.
        """
            
        self.rename_label = tk.Label(self._frame, text = 'Rename the file:', font = self.LYRICS[1], fg = 'red')
        self.rename_label.grid(row = 5, column = 0, sticky = 'e', padx = 5)
            
        self.rename = tk.Entry(self._frame, textvariable = self.RENAME, font = self.LYRICS[1])
        self.rename.grid(row = 5, column = 1, sticky = 'we', pady = 5)
        
        
    def _update_type(self):
        """ Private function that checks the type chosen and 
        update the window with the new type chosen.
        """
                    
        if self.TYPES.get() == 'Anything!' or self.TYPES.get() == 'Youtube':
            self._rename()
                        
        else:
            self.rename_label.destroy()
            self.rename.destroy()
        
    
    def _download(self):
        """ Private function manager of initialize the module called
        'download.py' and 'connection_db.py'.
        """
        
        if self.URL.get() == '' or self.TYPES.get() == 'Types':
             self._error_01() # Call error function
             
        else:  
            DataBase(self.URL, self.TYPES, self.RENAME, self.PATH_DIR, self.MKDIR, self.HISTORY) 
            Download(self._root, self._canvas, self._frame, self.URL, self.TYPES, self.RENAME, self.PATH_DIR, 
                     self.LYRICS, self.MKDIR, self.HISTORY)
        
        
    def _error_01(self):
        """ Private function manager of show the error
        number 01.
        """
            
        error_01_text = 'Please complete all the Required fields!' # Text
                
        self.error_01_label = tk.Label(self._frame, text = error_01_text, font = self.LYRICS[1], fg = 'red', wraplength = 400)
        self.error_01_label.grid(row = 9, columnspan = 4, sticky = 'we', pady = 10)             

        self.error_01_label.after(5000, self.error_01_label.destroy) # Destroy error after 5 seconds
                
        
def _getit():
    """ Private function that handle the engine of 
    the program
    """
    
    root = tk.Tk()
    MainClass(root)
    root.mainloop()


if __name__ == '__main__':
    _getit() # Starts the execution