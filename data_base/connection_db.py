""" All libraries and modules imported """

# Sqlite3 library
import sqlite3


class ConnectionClass(object):
    """ Class connection data base manager """
    
    def __init__(self, Url, Types, Rename, Path, Mkdir, History):
        """ Main initial method of connection data base """
        
        # Constants variables
        self.URL = Url
        self.TYPES = Types 
        self.RENAME = Rename
        self.PATH_DIR = Path
        self.MKDIR = Mkdir
        self.HISTORY = History
        
        if self.RENAME.get() == '':
            self.RENAME = 'my_download'
            self.DATES = (self.URL.get(), self.HISTORY.get(), self.TYPES.get(), self.RENAME, self.PATH_DIR, 
                          self.MKDIR.get())
        
        else:
            self.DATES = (self.URL.get(), self.HISTORY.get(), self.TYPES.get(), self.RENAME.get(), self.PATH_DIR, 
                          self.MKDIR.get())
        
        
        # Data base connection and dates insertion 
        try:
            connect_db = sqlite3.connect('./data_base/url_recovery.sqlite3')
            cursor_db = connect_db.cursor()
                
            cursor_db.execute(
                ''' CREATE TABLE backups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL,
                    track INTEGER NOT NULL,  
                    type TEXT NOT NULL,
                    rename TEXT NOT NULL,
                    path TEXT NOT NULL,
                    folder INTERGER NOT NULL,
                    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    active TINYINT(1) NOT NULL DEFAULT '1'
                ) '''
            )

            cursor_db.execute('INSERT INTO backups (url, track, type, rename, path, folder) VALUES (?, ?, ?, ?, ?, ?)', 
                              self.DATES) 
            
        except (sqlite3.OperationalError, sqlite3.InterfaceError):
            cursor_db.execute('INSERT INTO backups (url, track, type, rename, path, folder) VALUES (?, ?, ?, ?, ?, ?)', 
                              self.DATES)  
                
        finally:
            connect_db.commit()
            connect_db.close()                  