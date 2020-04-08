""" All libraries and modules imported """

# Tkinter libraries
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


# Pytube library
import pytube


class DownloadClass(tk.Tk):
    """ Class download manager """
    
    def __init__(self, Root, Frame, Url, Types, Path, Lyrics):
        """ Main initial method of download """
        
        # Assignament variables
        self._root = Root
        self._frame = Frame
        
        
        # Constants variables
        _URL = Url
        _TYPES = Types 
        _PATH_DIR = Path
        _LYRICS = Lyrics
        
        
        # Constants funtions
        def _progress_bar():
            """ Private funtion manager of show the progress
            bar when the download starts.
            """
            
            bar = ttk.Progressbar(self._frame, orient = 'horizontal', length = 100, mode = 'determinate', value = 85)
            bar.config(takefocus = True)
            bar.grid(row = 6, columnspan = 2, sticky = 'we', pady = 10)
            
            
        def _downloaded():
            """ Private funtion manager of show the path of the
            downloaded files.
            """
            
            _thank_you = f'The download has finished, you can find it in: \n\n{_PATH_DIR} \n\nHave a nice day!' # Thanks
            
            loaded = tk.Label(self._frame, text = _thank_you, font = _LYRICS[1], fg = 'red', wraplength = 500)
            loaded.grid(row = 7, columnspan = 2, sticky = 'we')
            
            self._root.update() # Update the window
        
        # URL download 
        if _TYPES.get() == 'URL':
            pass
        
        
        # YouTube download
        elif _TYPES.get() == 'Youtube':
            if _PATH_DIR:
                # Starts the progress bar and update the window
                _progress_bar() 
                self._root.update()
                
                
                # Starts youtube download and save it 
                yt_video = pytube.YouTube(_URL.get())                
                yt_dir = yt_video.streams.first().download(_PATH_DIR)
                
                
                # Show the path and thank you
                _downloaded()
                
                    
        # Torrent download
        elif _TYPES.get() == 'Torrent':
            pass
        
        
        # Update the window    
        self._root.update()        