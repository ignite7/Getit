""" All libraries and modules imported """

# Tkinter libraries
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


# Important libraries
import pytube # Youtube
import urllib.request # Url download
import time # Take the time


class DownloadClass(tk.Tk):
    """ Class download manager """
    
    def __init__(self, Root, Canvas, Frame, Url, Types, Rename, Path, Lyrics):
        """ Main initial method of download """
        
        # Assignament variables
        self._root = Root
        self._canvas = Canvas
        self._frame = Frame
        
        
        # Constants variables
        _URL = Url
        _TYPES = Types 
        _RENAME = Rename
        _PATH_DIR = Path
        _LYRICS = Lyrics
        
        
        # Update window
        def _update_window(self):
            """ Private funtion managet to update the window 
            of the program.
            """
            
            self._root.update()  
            self._canvas.config(scrollregion = self._canvas.bbox('all'))
            self._canvas.pack()
            self._frame.pack()
        
        
        # Errors messages
        def _any_error(self):
            """ Private funtion exclusive from this module.
            Starts when the 'URL' can't be downloaded.
            """
            
            _any_error_text = [
                'Something was wrong! \n\n The URL doesn\'t accept downloads'
                '\n\nConsult the provider of the URL.'
            ]
            
            self.any_error = tk.Label(self._frame, text = _any_error_text[0], font = _LYRICS[1])
            self.any_error.config(fg = 'red', wraplength = 500)
            self.any_error.grid(row = 11, columnspan = 2, sticky = 'we', pady = 10)
            
        
        # Constants funtions
        def _progress_bar(self):
            """ Private funtion manager of show the progress
            bar when the download starts.
            """
            
            self.bar = ttk.Progressbar(self._frame, orient = 'horizontal', length = 100, mode = 'determinate')
            self.bar.config(takefocus = True)
            self.bar.grid(row = 9, columnspan = 2, sticky = 'we', pady = 10)
            
            self.wait = tk.Label(self._frame, text = 'Downloading...', font = _LYRICS[1], fg = 'red')
            self.wait.grid(row = 10, columnspan = 2, sticky = 'we')
            
            _updating_progress_bar(self) # Update of the progress bar
            
            return self.bar
        
        
        def _updating_progress_bar(self):
            """ Private funtion manager of update the progress
            bar.
            """
            
            for updating in range(0, 81, 20):
                self.bar['value'] = updating
                _update_window(self)
                time.sleep(1)
            
                
        def _downloaded(self):
            """ Private funtion manager of show the path of the
            downloaded files.
            """
            
            _thank_you = f'The download has finished, you can find it in: \n\n{_PATH_DIR} \n\nHave a nice day!' # Thanks
            
            self.loaded = tk.Label(self._frame, text = _thank_you, font = _LYRICS[1], fg = 'red', wraplength = 500)
            self.loaded.grid(row = 11, columnspan = 2, sticky = 'we', pady = 10)
            
            
            # Finish progress bar
            self.bar['value'] = 100
            time.sleep(2)
            
            
            # Destory text 'Wait...' and label indicating that has been completed
            self.wait.destroy()
            
            self.completed = tk.Label(self._frame, text = 'Completed!', font = _LYRICS[1], fg = 'red')
            self.completed.grid(row = 10, columnspan = 2, sticky = 'we')
            
            _update_window(self) # Update window
            
            return self.loaded

        
        def _clear_all_completed(self):
            """ Private funtion manager of clean the window with 
            the default values.
            """
            
            _URL.set('')
            _TYPES.set('Types')
            _RENAME.set('')
            _PATH_DIR = None
            
            
            # Destory the progress, completed and the thanks message after 8 seconds
            self.bar.after(8000, self.bar.destroy)
            self.loaded.after(8000, self.loaded.destroy)
            self.completed.after(8000, self.completed.destroy)      
        
        
        def _clear_all_uncompleted(self):
            """ Private funtion manager of clean the window when
            the download has failed.
            """
            
            _URL.set('')
            _TYPES.set('Types')
            _RENAME.set('')
            _PATH_DIR = None
            
            
            # Destory the progress, completed and the error after 8 seconds
            self.bar.destroy()
            self.wait.destroy()
            self.any_error.after(8000, self.any_error.destroy)
        
        
        try:
            def _url_downloads():
                """ Private funtion manager of downloads the types
                'URL' and 'Torrent' from the options.
                """
            
                # Re-assignament variables and starts progress bar
                _progress_bar(self)
                rename = _RENAME.get()
                url = _URL.get()

                
                # Request and content of the file
                response = urllib.request.urlopen(url)
                content = response.read()
                
                
                # Save the file and check the url type
                if rename != '': 
                    with open(f'{_PATH_DIR}/{rename}', 'wb') as downloaded:
                        downloaded.write(content)

                else:
                    with open(f'{_PATH_DIR}/download_getit', 'wb') as downloaded:
                        downloaded.write(content)
                    
                        
                # Show the resume
                _downloaded(self)
                _clear_all_completed(self)
            
                
            # URL download 
            if _TYPES.get() == 'URL':
                _url_downloads() # Call private funtion
            
            
            # YouTube download
            elif _TYPES.get() == 'Youtube':
                # Starts the progress bar and update the window
                _progress_bar(self) 
                self._root.update()
                
                
                # Starts youtube download and save it 
                try:
                    yt_video = pytube.YouTube(_URL.get())                
                    yt_video.streams.first().download(_PATH_DIR)
                
                except DeprecationWarning:
                    pass # Do nothing with warning
                
                
                # Show the path, clear all and thanks
                _downloaded(self)
                _clear_all_completed(self)
       
                
            # YT Playlist download
            elif _TYPES.get() == 'YT Playlist':
                # Starts the progress bar and update the window
                _progress_bar(self)
                self._root.update()
            
            
                # Starts YT Playlist download and save it
                try:
                    yt_playlist = pytube.Playlist(_URL.get())
                    yt_playlist.download_all(_PATH_DIR)
            
                except DeprecationWarning:
                    pass # Do nothing with warning
            
            
                # Show the path, clear all and thanks
                _downloaded(self)
                _clear_all_completed(self)
         
                             
            # Torrent download
            elif _TYPES.get() == 'Torrent':
                _url_downloads() # Call private funtion
        
        except:
            _any_error(self) # Call exclusive private funtion 
            _clear_all_uncompleted(self) # Clear everything
            
            
        # Update the window    
        _update_window(self)  