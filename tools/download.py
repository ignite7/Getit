""" All libraries and modules imported """

# Tkinter libraries
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


# System info 
import platform
import sys
import os
import shutil


# Important libraries
import pytube # Youtube
import requests
import time # Take the time


# Modules
from .wrappers.decorate import DecorateClass as Decorate


class DownloadClass(tk.Tk):
    """ Class download manager """
    
    def __init__(self, Root, Canvas, Frame, Url, Types, Rename, Path, Lyrics, Mkdir, History):
        """ Main initial method of download """
        
        # Assignament variables
        self._root = Root
        self._canvas = Canvas
        self._frame = Frame
        
        
        # Constants variables
        self.URL = Url
        self.TYPES = Types 
        self.RENAME = Rename
        self.PATH_DIR = Path
        self.LYRICS = Lyrics
        self.MKDIR = Mkdir
        self.HISTORY = History
            
        if self.MKDIR.get():
            if sys.platform.startswith('linux'):
                os.makedirs(f'{self.PATH_DIR}/download_getit', exist_ok=True)
                self.DIR = f'{self.PATH_DIR}/download_getit'
                
            else: 
                os.makedirs(f'{self.PATH_DIR}\\download_getit', exist_ok=True)
                self.DIR = f'{self.PATH_DIR}\\download_getit'
            
        else: 
            self.DIR = self.PATH_DIR
        
        # Downloads options
        try:
            if self.HISTORY.get():
                self._requests()
                
                with open(f'{self.DIR}/history.txt', 'w') as history_url:
                    history_url.write(
                        f'URL: {self.response.url}\n'
                        f'STATUS CODE: {self.response.status_code}\n'
                        f'HEADERS: {self.response.headers}'
                    )
                    
                    
            # URL download 
            if self.TYPES.get() == 'Anything!':
                self._url_downloads() # Call private function
            
            
            # YouTube download
            elif self.TYPES.get() == 'Youtube':
                # Starts the progress bar, assignament variable and update the window
                self._progress_bar()
                self._root.update()
                rename = self.RENAME.get()
                
                
                # Starts youtube download and save it
                yt_video = pytube.YouTube(self.URL.get())                
                route = yt_video.streams.filter(res = '720p').first().download(self.DIR)
                
                if rename == '':
                    shutil.move(route, route)
                
                elif not rename.endswith('.mp4'):
                    shutil.move(route, f'{self.DIR}/{rename}.mp4')
                    
                else:
                    shutil.move(route, f'{self.DIR}/{rename}')
                
                
                # Show the path, clear all and thanks
                self._downloaded()
                self._clear_all_completed()
       
                
            # YT Playlist download
            elif self.TYPES.get() == 'YT Playlist':
                # Starts the progress bar and update the window
                self._progress_bar()
                self._root.update()
            
            
                # Starts YT Playlist download and save it
                yt_playlist = pytube.Playlist(self.URL.get())
                yt_playlist.download_all(self.DIR, resolution = '720p')
            
            
                # Show the path, clear all and thanks
                self._downloaded()
                self._clear_all_completed()
                
    
        except:
            self._any_error() # Call exclusive private function 
            self._clear_all_uncompleted() # Clear everything
            os.rmdir(self.DIR)
          
            
        # Update the window    
        self._update_window()
 
        
    def _update_window(self):
        """ Private function managet to update the window 
        of the program.
        """
            
        self._root.update()  
        self._canvas.config(scrollregion = self._canvas.bbox('all'))
        self._canvas.pack()
        self._frame.pack()
        
        
    def _updating_progress_bar(self):
        """ Private function manager of update the progress
        bar.
        """
            
        for updating in range(0, 81, 20):
            self.bar['value'] = updating
            self._update_window()
            time.sleep(1)
            
                
    def _progress_bar(self):
        """ Private function manager of show the progress
        bar when the download starts.
        """
            
        self.bar = ttk.Progressbar(self._frame, orient = 'horizontal', length = 100, mode = 'determinate')
        self.bar.config(takefocus = True)
        self.bar.grid(row = 9, columnspan = 2, sticky = 'we', pady = 10)
            
        self.wait = tk.Label(self._frame, text = 'Downloading...', font = self.LYRICS[1], fg = 'red')
        self.wait.grid(row = 10, columnspan = 2, sticky = 'we')
        
        self._updating_progress_bar() # Update of the progress bar
        
       
    def _downloaded(self):
        """ Private function manager of show the path of the
        downloaded files.
        """
            
        thank_you = f'The download has finished, you can find it in: \n\n{self.DIR} \n\nHave a nice day!' # Thanks
            
        self.loaded = tk.Label(self._frame, text = thank_you, font = self.LYRICS[1], fg = 'red', wraplength = 500)
        self.loaded.grid(row = 11, columnspan = 2, sticky = 'we', pady = 10)
            
            
        # Finish progress bar
        self.bar['value'] = 100
        time.sleep(1)
            
            
        # Destory text 'Wait...' and label indicating that has been completed
        self.wait.destroy()
            
        self.completed = tk.Label(self._frame, text = 'Completed!', font = self.LYRICS[1], fg = 'red')
        self.completed.grid(row = 10, columnspan = 2, sticky = 'we')
            
        self._update_window() # Update window
        
    
    def _requests(self):
        """ Private method manager of download the url
        of internet and allow redirects.
        """
        
        self.response = requests.get(self.URL.get(), allow_redirects = True)
 
        
    def _url_downloads(self):
        """ Private function manager of downloads the types
        'Anything!' from the options.
        """
        
        # Re-assignament variables and starts progress bar
        self._progress_bar()
        rename = self.RENAME.get()
        self._requests() # Request and content of the file


        # Save the file and check the url type
        if rename != '':    
            with open(f'{self.DIR}/{rename}', 'wb') as downloaded:
                downloaded.write(self.response.content)
          
        else:
            with open(f'{self.DIR}/my_download', 'wb') as downloaded:
                downloaded.write(self.response.content)
        
                            
        # Show the resume
        self._downloaded()
        self._clear_all_completed()  
        
     
    @Decorate._decorator_clear_all
    def _clear_all_completed(self):
        """ Private function manager of clean the window with 
        the default values.
        """
            
        self.bar.after(8000, self.bar.destroy)
        self.loaded.after(8000, self.loaded.destroy)
        self.completed.after(8000, self.completed.destroy)      
        
   
    @Decorate._decorator_clear_all
    def _clear_all_uncompleted(self):
        """ Private function manager of clean the window when
        the download has failed.
        """

        self.bar.destroy()
        self.wait.destroy()
        self.any_error.after(10000, self.any_error.destroy)
        

    def _any_error(self):
        """ Private function exclusive from this module.
        Starts when the 'URL' can't be downloaded.
        """
            
        any_error_text = [
            'Something was wrong! Check the manual.'
            '\n\nThe URL doesn\'t accept downloads, consult the provider of the URL.'
            '\n\nAlso you make sure the file to download has permissions to save on your computer.'
        ]
            
        self.any_error = tk.Label(self._frame, text = any_error_text[0], font = self.LYRICS[1])
        self.any_error.config(fg = 'red', wraplength = 450)
        self.any_error.grid(row = 11, columnspan = 2, sticky = 'we', pady = 10)