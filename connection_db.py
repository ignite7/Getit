""" All libraries and modules imported """

# System info
import platform
import sys


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
        
        # Data base connection
        connect_db = sqlite3.connect('./url_recovery.sqlite3')
        cursor_db = connect_db.cursor()
        
        
        # Data base creation
        try:
            cursor_db.execute(
                ''' CREATE TABLE backups (
                        id INT AUTO_INCREMENT,
                        type VARCHAR(30) NOT NULL,
                        rename VARCHAR(100) NOT NULL,
                        path VARCHAR(100) NOT NULL,
                        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        active TINYINT(1) NOT NULL DEFAULT '1',
                        PRIMARY KEY (id)  
                ) '''
            )

        except sqlite3.OperationalError:
            pass
                
        connect_db.close() # Connection closed