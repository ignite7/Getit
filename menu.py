""" All libraries and modules imported """

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class MenuClass(tk.Tk):
    """ Class menu manager """
    
    def __init__(self, Root, *args, **kwargs):
        """ Main initial method of menu """
        
        # Assignament variables
        self._root = Root
        
        # Assignament menu
        menu = tk.Menu(self._root)
        self._root.config(menu = menu)
        
        # Option help
        menu_help = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = 'Options', menu = menu_help)
        
        menu_help.add_command(label = 'Help')
        menu_help.add_separator()
        menu_help.add_command(label = 'Version')
        menu_help.add_command(label = 'About')
        menu_help.add_separator()
        menu_help.add_command(label = 'Exit')