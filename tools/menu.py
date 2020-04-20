""" All libraries and modules imported """

# Tkinter 
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


# System info
import platform
import sys


# Modules
from .wrappers.decorate import DecorateClass as Decorate


class MenuClass(tk.Tk):
    """ Class menu manager """
    
    def __init__(self, Root, Url, Types, Rename, Path, Lyrics, Recovery, Mkdir, History):
        """ Main initial method of menu """
        
        # Assignament variables
        self._root = Root
        
        
        # Constants variables
        self.URL = Url
        self.TYPES = Types 
        self.RENAME = Rename
        self.PATH_DIR = Path
        self.LYRICS = Lyrics
        self.RECOVERY = Recovery
        self.MKDIR = Mkdir
        self.HISTORY = History
        
        
        # Assignament menu
        menu = tk.Menu(self._root)
        self._root.config(menu = menu)
        
        
        # Help
        menu_help = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = 'Help', menu = menu_help)
        
        menu_help.add_command(label = 'Manual', command = lambda: HelpClass(self._root, self.LYRICS))
        menu_help.add_separator()
        menu_help.add_command(label = 'Version', command = lambda: self._version())
        menu_help.add_command(label = 'About Me', command = lambda: self._about_me())
        menu_help.add_separator()
        menu_help.add_command(label = 'Exit', command = lambda: self._exit())
        
        
        # Options
        menu_options = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = 'Options', menu = menu_options)
        
        menu_options.add_command(label = 'URL Recovery', command = self.RECOVERY)
        menu_options.add_command(label = 'Clear Fields', command= lambda: self._clear_everything())
    
    
    def _version(self):  
        """ Private function manager to show
        the version of the program.
        """
          
        version = messagebox.showinfo(
            parent = self._root,
            title = 'Version',
            message = 'Program Version: 1.0 \n\nLenguage Version: Python-3.8.X'
        )


    def _about_me(self):  
        """ Private function manager to show
        the about me of the program.
        """
          
        about_me = messagebox.showinfo(
            parent = self._root,
            title = 'About Me',
            message = 'Author: Sergio van Berkel Acosta \n\nContact: www.sergiovanberkel.com'
        )


    def _exit(self):
        """ Private function manager to show
        the exit of the program.
        """
        
        leave = messagebox.askquestion(
            parent = self._root,
            title = 'Exit',
            message = 'Do you want to leave of the program?'
        )      
        
        if leave == 'yes':
            self._root.destroy()
    
    
    @Decorate._decorator_clear_all      
    def _clear_everything(self):
        """ Private method manager to clear
        everything in the fields.
        """
    
        everything_clear = messagebox.showinfo(
            parent = self._root,
            title = 'Cleaned',
            message = 'Everything has been cleaned!'
        )
                       
                           
class HelpClass(tk.Tk):
    """ Class help manager """
    
    def __init__(self, Root, Lyrics):
        """ Main initial method of Help """
        
        # Assignament variables
        self._root = Root
        self.LYRICS = Lyrics

        
        # ICO image for windows
        if sys.platform.startswith('win32'):
            self._root.iconbitmap('.\\img\\icon.ico')
            
            
        # Window
        self._main_window = tk.Toplevel(self._root)
        self._main_window.title('Manual')
        self._main_window.geometry('600x650')
        self._main_window.resizable(False, False)
        
        
        # Canvas and frame 
        self._canvas = tk.Canvas(self._main_window)
        self._frame = tk.Frame(self._canvas)
        
        
        # Image
        if sys.platform.startswith('linux'):
            self.manual = ImageTk.PhotoImage(Image.open('./img/manual.png'))
            self._logo_complement()
            
        else:
            self.manual = ImageTk.PhotoImage(Image.open('.\\img\\manual.png'))
            self._logo_complement()
            
            
        # Texts
        TEXTS = [
            (
                'The purpose of this program is makes your life more easy, '
                'but please read the instructions to you don\'t make mistakes.'
             ),
            (
                '01 - You make sure that the \'URL\' is the correct and the file to download has permissions.'
                '\n\n'
                '02 - The only fields that aren\'t necessary fill out are \'RENAME\' field and \'OPEN FOLDER\' field.'
                '\n\n'
                '03 - If you rename your file please puts the correct extension of the file.'
                '\n\n'
                '04 - You can update your choise selecting a new type and the click in the button \'UPDATE THE TYPE\'.'
                '\n\n'
                '05 - REMEMBER to be patient with the download because depends of your internet conection '
                'and REMEMBER sometimes there are URL\'s that have firewalls or locks, '
                'consult the provider of the URL if you have problems.'
                '\n\n'
                '06 - You can copy and remove your old downloads in the options of the menu \'URL RECOVERY\'.'
                '\n\n'
                '07 - If you want more information you can contact me in www.sergiovanberkel.com.'
                '\n\n'
                '08 - And finally thank you for uses this program!'
            )
        ]
        
        
        # Instructions
        instructions = tk.Label(self._frame, text = TEXTS[0], font = self.LYRICS[0], justify = 'center', wraplength = 500)
        instructions.grid(row = 1, column = 0, sticky = 'we', pady = 20)
        
        rules = tk.Label(self._frame, text = TEXTS[1], font = self.LYRICS[1], justify = 'left', wraplength = 500)
        rules.grid(row = 2, column = 0, sticky = 'we', pady = 10)


        # Update window    
        self._update_window()   
        
        
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
            
        self.manual_label = tk.Label(self._frame, image = self.manual)
        self.manual_label.image = self.manual # Reference
        self.manual_label.grid(row = 0, columnspan = 1, column = 0, sticky = 'nswe', pady = 20)