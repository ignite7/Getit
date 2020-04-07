""" All libraries and modules imported """

# Tkinter 
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


# Sys info
import platform
import sys


# Modules
from menu import MenuClass
from download import DownloadClass


class MainClass(tk.Tk):
    """ Main Class of the window, and executor of
    another variables
    """
    
    def __init__(self, Root, *args, **kwargs):
        """ Method of init when the program starts """  
            
        # Assigment variables
        self._root = Root
        self._root.title('Getit')
        self._root.geometry('600x500')
         
        self._scroll = tk.Scrollbar(self._root)
        self._canvas = tk.Canvas(self._root, yscrollcommand = self._scroll.set)

        self._scroll.config(command = self._canvas.yview)
        self._scroll.pack(side = 'right', fill = 'y')

        self._frame = tk.Frame(self._canvas)
        self._canvas.create_window(0, 0, window = self._frame, anchor = 'center')
        
        
        # Lyrics
        _LYRICS = (
            ('Courier New', 12, 'bold'),
            ('Courier New', 11, 'normal'),
            ('Courier New', 11, 'italic')
        )
        
        
        # Contants variables inserts
        _URL = tk.StringVar()
        _TYPES = tk.StringVar()
        _START = tk.IntVar()
        
          
        # Image
        if sys.platform.startswith('linux'):
            logo = ImageTk.PhotoImage(Image.open('./img/logo.png'))
            logo_label = tk.Label(self._frame, image = logo, cursor = 'hand2')
            logo_label.image = logo # Reference
            logo_label.grid(row = 0, columnspan = 2, column = 0, sticky = 'nswe', pady = 20)
            
        else:
            logo = ImageTk.PhotoImage(Image.open('.\\img\\logo.png'))
            logo_label = tk.Label(self._frame, image = logo, cursor = 'hand2')
            logo_label.image = logo # Reference
            logo_label.grid(row = 0, columnspan = 2, column = 0, sticky = 'nswe', pady = 20)
        
                
        # Introduce cell   
        introduce_label = tk.Label(self._frame, text = 'Get anything from URL to your computer!', font = _LYRICS[0])
        introduce_label.grid(row = 1, columnspan = 2, sticky = 'we', pady = 10)
        
        
        # Url cell
        url_label = tk.Label(self._frame, text = 'Your URL:', font = _LYRICS[2])
        url_label.grid(row = 2, column = 0, sticky = 'e', padx = 5)
        
        url = tk.Entry(self._frame, textvariable = _URL, font = _LYRICS[1])
        url.grid(row = 2, column = 1, sticky = 'we', pady = 5)
        
        
        # Choose type cell
        sort_label =  tk.Label(self._frame, text = 'Choose the type:', font = _LYRICS[1])
        sort_label.grid(row = 3, column = 0, sticky = 'e', padx = 5)
        
        _TYPES.set('Types')
        list_of_types = ['URL', 'Youtube', 'Torrent']
        
        sort = tk.OptionMenu(self._frame, _TYPES, *list_of_types)
        sort.config(font = _LYRICS[1], relief = 'groove', borderwidth = 2)
        sort.grid(row = 3, column = 1, sticky = 'we', pady = 5)
        
        
        # Save the path
        save_label = tk.Label(self._frame, text = 'Where do you want save it?', font = _LYRICS[1])
        save_label.grid(row = 4, column = 0, sticky = 'e', padx = 5)
    
        save = tk.Button(self._frame, text = 'Open', cursor = 'hand2', command = lambda:_open_dir())
        save.config(relief = 'groove', borderwidth = 2, font = _LYRICS[1])
        save.grid(row = 4, column = 1, sticky = 'we', pady = 5)
        
        
        def _open_dir():
            """ Funtion manager of establish the path of the dir
            where save the files downloads.
            """
            
            if sys.platform.startswith('linux'):
                file_dialog = filedialog.askdirectory(
                    parent = self._frame, 
                    title = 'Choose The Directory', 
                    initialdir = '~/'
                )

            else: 
                file_dialog = filedialog.askdirectory(
                    parent = self._frame, 
                    title = 'Choose The Directory', 
                    initialdir = 'C:\\Downloads'
                )
        
        # Start button
        _START.set('Start!') # Button text 
        button = tk.Button(self._frame, textvariable = _START, cursor = 'hand2', command = lambda:_download())
        button.config(relief = 'groove', borderwidth = 2, font = _LYRICS[1])
        button.grid(row = 5, columnspan = 2, sticky = 'we', pady = 10)
        
        
        def _download():
            DownloadClass(self._root, self._frame, _LYRICS) # Module 'download.py'
        
        # Update and grid of the window
        self._root.update()
        self._canvas.config(scrollregion = self._canvas.bbox('all'))
        self._canvas.pack() # (side = 'left', fill = 'both', expand = True)
        self._frame.pack()
        
        
        # Calls class
        MenuClass(self._root) # Module 'menu.py'
        
        # Help objects
        #print(dir(introduce))

        
def _main_funtion():
    """ Funtion that handle the engine of 
    the program
    """
    
    root = tk.Tk()
    getit = MainClass(root)
    root.mainloop()


if __name__ == '__main__':
    _main_funtion() # Zero Init