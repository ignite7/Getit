""" All libraries and modules imported """

# Tkinter 
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


# System info
import platform
import sys


class MenuClass(tk.Tk):
    """ Class menu manager """
    
    def __init__(self, Root, Url, Types, Rename, Path, Lyrics):
        """ Main initial method of menu """
        
        # Assignament variables
        self._root = Root
        
        
        # ICO image for windows
        if sys.platform.startswith('win'):
            self._root.iconbitmap('.\\img\\icon.ico')
        
        
        # Constants variables
        _URL = Url
        _TYPES = Types 
        _RENAME = Rename
        _PATH_DIR = Path
        _LYRICS = Lyrics
        
        
        # Assignament menu
        menu = tk.Menu(self._root)
        self._root.config(menu = menu)
        
        
        # Option help
        menu_help = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = 'Help', menu = menu_help)
        
        menu_help.add_command(label = 'Manual', command = lambda: _help())
        menu_help.add_separator()
        menu_help.add_command(label = 'Version', command = lambda: _version())
        menu_help.add_command(label = 'About Me', command = lambda: _about_me())
        menu_help.add_separator()
        menu_help.add_command(label = 'Exit', command = lambda: _exit())
        
        
        # Option recovery url
        menu_options = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = 'Options', menu = menu_options)
        
        menu_options.add_command(label = 'Recovery URL')
        
        
        # Menu funtions
        def _help():
            HelpClass(self._root, _LYRICS)
            
        
        def _version():
            VersionClass(self._root)
            
        
        def _about_me():
            AboutMeClass(self._root)
            
        
        def _exit():
            ExitClass(self._root)    
            
                       
class HelpClass(tk.Tk):
    """ Class help manager """
    
    def __init__(self, Root, Lyrics):
        """ Main initial method of Help """
        # Assignament variables
        self._root = Root
        
        
        # Constants variables
        _LYRICS = Lyrics
        
        
        # Window
        self._main_window = tk.Toplevel(self._root)
        self._main_window.title('Manual')
        self._main_window.geometry('600x600')
        self._main_window.resizable(False, False)
        
        
        # Canvas, frame and scroll bar
        _scroll = tk.Scrollbar(self._main_window)
        self._canvas = tk.Canvas(self._main_window, yscrollcommand = _scroll.set)
        
        _scroll.config(command = self._canvas.yview)
        _scroll.pack(side = 'right', fill = 'y')
        
        self._frame = tk.Frame(self._canvas)
        self._canvas.create_window(0, 0, window = self._frame, anchor = 'nw')
        
        
        # Constants funtions
        def _update_window(self):
            """ Private funtion managet to update the window 
            of the program.
            """
            
            self._main_window.update()
            self._canvas.config(scrollregion = self._canvas.bbox('all'))
            self._canvas.pack()
            self._frame.pack()
        
        
        # Short part of code of the logo
        def _manual_complement():
            """ Private funtion manager to complement the 
            manual image.
            """
            
            manual_label = tk.Label(self._frame, image = manual)
            manual_label.image = manual # Reference
            manual_label.grid(row = 0, columnspan = 1, column = 0, sticky = 'nswe', pady = 20)
         
            
        # Image
        if sys.platform.startswith('linux'):
            manual = ImageTk.PhotoImage(Image.open('./img/manual.png'))
            _manual_complement()
            
        else:
            manual = ImageTk.PhotoImage(Image.open('.\\img\\manual.png'))
            _manual_complement() 
        
        
        # Texts
        _TEXTS = [
            (
                'The purpose of this program is makes your life more easy, '
                'but please read the instructions to you don\'t make mistakes.'
             ),
            (
                '01 - You should make sure that the \'URL\' is the correct.'
                '\n\n'
                '02 - The only fields that\ aren\'t necessary fill out are \'RENAME\' field and \'OPEN FOLDER\' field.'
                '\n\n'
                '03 - If you rename your file please puts the correct extension of the file.'
                '\n\n'
                '04 - You can update your choise selecting a new type and the click in the button \'UPDATE THE TYPE\'.'
                '\n\n'
                '05 - Remember to be patient with the download because depends of your internet conection.'
                '\n\n'
                '06 - If you want more information you can contact me in www.sergiovanberkel.com.'
                '\n\n'
                '07 - And finally thank you for uses this program!'
            )
        ]
        
        
        # Instructions
        instructions = tk.Label(self._frame, text = _TEXTS[0], font = _LYRICS[0], justify = 'center', wraplength = 500)
        instructions.grid(row = 1, column = 0, sticky = 'we', pady = 20)
        
        rules = tk.Label(self._frame, text = _TEXTS[1], font = _LYRICS[1], justify = 'left', wraplength = 500)
        rules.grid(row = 2, column = 0, sticky = 'we', pady = 10)


        # Update window    
        _update_window(self)


class VersionClass(tk.Tk):
    """ Class version manager """
    
    def __init__(self, Root):
        """ Main initial method of version """
        
        # Assignament variables
        self._root = Root
        
        
        # Version Message
        version = messagebox.showinfo(
            parent = self._root,
            title = 'Version',
            message = 'Program Version: 1.0 \n\nLenguage Version: Python-3.8.X'
        )


class AboutMeClass(tk.Tk):
    """ Class About manager """
    
    def __init__(self, Root):
        """ Main initial method of about """
        
        # Assignament variables
        self._root = Root

        
        # About me Message
        about_me = messagebox.showinfo(
            parent = self._root,
            title = 'About Me',
            message = 'Author: Sergio van Berkel Acosta \n\nContact: www.sergiovanberkel.com'
        )


class ExitClass(tk.Tk):
    """ Class About manager """
    
    def __init__(self, Root):
        """ Main initial method of exit """
    
        # Assignament variables
        self._root = Root
        
        
        # Exit Message
        exit = messagebox.askquestion(
            parent = self._root,
            title = 'Exit',
            message = 'Do you want to leave of the program?'
        )      
        
        if exit == 'yes':
            self._root.destroy()