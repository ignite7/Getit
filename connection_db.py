""" All libraries and modules imported """
# Sqlite3 library
import sqlite3


class ConnectionClass(object):
    """ Class connection data base manager """
    
    def __init__(self, Url, Types, Rename, Path):
        """ Main initial method of connection data base """
        
        # Constants variables
        _URL = Url
        _TYPES = Types 
        _RENAME = Rename
        _PATH_DIR = Path
        _DATES = (_URL.get(), _TYPES.get(), _RENAME.get(), _PATH_DIR)
        
        
        # Data base connection and dates insertion 
        try:
            connect_db = sqlite3.connect('./url_recovery.sqlite3')
            cursor_db = connect_db.cursor()
                
            cursor_db.execute(
                ''' CREATE TABLE backups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT,
                    type TEXT,
                    rename TEXT,
                    path TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    active TINYINT(1) DEFAULT '1'
                ) '''
            )

            cursor_db.execute('INSERT INTO backups (url, type, rename, path) VALUES (?, ?, ?, ?)', _DATES) 
            
        except sqlite3.OperationalError:
            cursor_db.execute('INSERT INTO backups (url, type, rename, path) VALUES (?, ?, ?, ?)', _DATES)  
                
        finally:
            connect_db.commit()
            connect_db.close()                  