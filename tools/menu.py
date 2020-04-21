""" All libraries and modules imported """

# Tkinter 
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


# System info
import platform
import sys


# Sqlite3 library
import sqlite3


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
            message = 'Program Version: 2.0 \n\nLenguage Version: Python-3.8.X'
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
        TEXT = [
            (
                'The purpose of this program is makes your life more easy, '
                'but please read the instructions to you don\'t make mistakes.'
             )
        ]
        
        
        # Instructions
        instructions = tk.Label(self._frame, text = TEXT[0], font = self.LYRICS[0], justify = 'center', wraplength = 500)
        instructions.grid(row = 1, column = 0, sticky = 'we', pady = 20)
        
        
        # Listbox and scrollbars
        v_scrollbar = tk.Scrollbar(self._frame, orient = 'vertical')
        v_scrollbar.grid(row = 2, column = 4, sticky = 'ns')
        h_scrollbar = tk.Scrollbar(self._frame, orient = 'horizontal')
        h_scrollbar.grid(row = 3, columnspan = 4, sticky = 'we')
        
        self.rule = tk.Listbox(self._frame, width = 60, height = 20, cursor = 'hand2', font = self.LYRICS[1])
        self.rule.config(xscrollcommand = h_scrollbar.set, yscrollcommand = v_scrollbar.set)
        self.rule.config(selectmode = tk.SINGLE, borderwidth = 2)
        self.rule.grid(row = 2, columnspan = 1, sticky = 'we')
        
        v_scrollbar.config(command = self.rule.yview)
        h_scrollbar.config(command = self.rule.xview)
        
        
        # Show the dates inside of listbox
        space = ' ' * 20
        self.rule.insert(tk.END, f'[Nº]{space}[RULE DESCRIPTION]')
        self._show_rules()
        

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
        
    
    @Decorate._instructions_db
    def _show_rules(self):
        """ Private method manager to show
        the instructions in the textlist.
        """
        
        try:
            self.cursor_db.execute('SELECT id, rule_description FROM instructions')
            self.print_db = self.cursor_db.fetchall()
        
            dates = [date[:] for date in self.print_db]
            for idx, items in enumerate(dates):
                self.rule.insert(idx + 1, f'{items}')
                
        except (sqlite3.OperationalError, sqlite3.InterfaceError):
            error_db = messagebox.showerror(
                parent = self._main_window,
                title = 'Data Base Don\'t Found',
                message = 'The data base doesn\'t exist, read the instuctions in:\n sergiovanberkel.com.'
            )