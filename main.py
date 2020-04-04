""" All libraries import """

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class MainClass(tk.Tk):
    """ Main Class of the window, and executor of
    another variables
    """
    
    def __init__(self, Root, *args, **kwargs):
        """ Method of init when the program starts """
            
        # Assigment variables
        self._root = Root
        self._root.title('Getit')
        self._root.geometry('500x500')
         
        self._scroll = tk.Scrollbar(self._root)
        self._canvas = tk.Canvas(self._root, yscrollcommand = self._scroll.set)

        self._scroll.config(command = self._canvas.yview)
        self._scroll.pack(side = 'right', fill = 'y')

        self._frame = tk.Frame(self._canvas)
        self._canvas.create_window(0, 0, window = self._frame, anchor = 'nw')
        
        # Body graphical window
        introduce = tk.Label(self._frame, text = 'Get anything from URL to your computer!')
        introduce.grid(row = 0, column = 0, sticky = 'nswe', pady = 10)
        
        # Update and grid of the window
        self._root.update()
        self._canvas.config(scrollregion = self._canvas.bbox('all'))
        self._canvas.pack(side = 'left', fill = 'both', expand = True)

def main_funtion():
    """ Funtion that handle the engine of 
    the program
    """
    
    root = tk.Tk()
    getit = MainClass(root)
    root.mainloop()

if __name__ == '__main__':
    main_funtion() # Zero Init