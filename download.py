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
            
            bar.after(5000, bar.destroy) # Destory the bar after finish
            
            
        def _downloaded():
            """ Private funtion manager of show the path of the
            downloaded files.
            """
            
            _thank_you = f'The download has finished, you can find it in: \n\n{_PATH_DIR} \n\nHave a nice day!' # Thanks
            
            loaded = tk.Label(self._frame, text = _thank_you, font = _LYRICS[1], fg = 'red', wraplength = 500)
            loaded.grid(row = 7, columnspan = 2, sticky = 'we')
            
            loaded.after(5000, loaded.destroy) # Destory the bar after finish
            self._root.update() # Update the window

        
        def _clear_all():
            """ Private funtion manager of clean the window with 
            the default values.
            """
            
            _URL.set('')
            _TYPES.set('Types')
            _PATH_DIR = None
            
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
                try:
                    yt_video = pytube.YouTube(_URL.get())                
                    yt_video.streams.first().download(_PATH_DIR)
                
                except DeprecationWarning:
                    pass # Do nothing with warning
                
                
                # Show the path, clear all and thanks
                _downloaded()
                _clear_all()
                
                
        # YT Playlist download
        elif _TYPES.get() == 'YT Playlist':
            # Starts the progress bar and update the window
            _progress_bar()
            self._root.update()
            
            
            # Starts YT Playlist download and save it
            try:
                yt_playlist = pytube.Playlist(_URL.get())
                yt_playlist.download_all(_PATH_DIR)
            
            except DeprecationWarning:
                pass # Do nothing with warning
            
            
            # Show the path, clear all and thanks
            _downloaded()
            _clear_all()
         
                             
        # Torrent download
        elif _TYPES.get() == 'Torrent':
            pass
        
        
        # Update the window    
        self._root.update()        