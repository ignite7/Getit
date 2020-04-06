""" All libraries and modules imported """

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from menu import MenuClass


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
        _title_lyric = 'Courier New', 12, 'bold'
        _normal_lyric = 'Courier New', 11, 'normal'
        _italic_lyric = 'Courier New', 11, 'italic'
        
        
        # Contants variables inserts
        _URL = tk.StringVar()
        _TYPES = tk.StringVar() 
        
          
        # Image
        
        
                
        # Introduce cell   
        introduce = tk.Label(self._frame, text = 'Get anything from URL to your computer!', font = _title_lyric)
        introduce.grid(row = 1, columnspan = 2, column = 0, sticky = 'we', pady = 30)
        
        
        # Url cell
        url_link = tk.Label(self._frame, text = 'Your URL:', font = _italic_lyric)
        url_link.grid(row = 2, column = 0, sticky = 'e', padx = 5)
        
        insert_url = tk.Entry(self._frame, textvariable = _URL, font = _normal_lyric)
        insert_url.grid(row = 2, column = 1, sticky = 'we')
        
        
        # Choose type cell
        type_cell =  tk.Label(self._frame, text = 'Choose the type:', font = _italic_lyric)
        type_cell.grid(row = 3, column = 0, sticky = 'e', padx = 5)
        
        _TYPES.set('Types')
        list_of_types = ['URL', 'Youtube', 'Torrent']
        
        choose = tk.OptionMenu(self._frame, _TYPES, *list_of_types)
        choose.config(font = _normal_lyric, relief = 'groove', borderwidth = 2)
        choose.grid(row = 3, column = 1, sticky = 'we')
        
        
        # Update and grid of the window
        self._root.update()
        self._canvas.config(scrollregion = self._canvas.bbox('all'))
        self._canvas.pack(side = 'left', fill = 'both', expand = True)
        self._frame.pack()
        
        
        # Call class 'Menu' of module 'Menu.py'
        MenuClass(self._root)
        
        
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