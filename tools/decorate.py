""" All libraries and modules imported """

# Sqlite3 library
import sqlite3


class DecorateClass(object):
    """ Class decorate manager to supply all
    decorators to the other modules.
    """
    
    @staticmethod
    def _connection_db(function):
        """ Decorate function manager to implement
        the connection with the data base.
        MODULE: tools.recovery
        """
            
        def wrapper(self):
            self.connect_db = sqlite3.connect('./data_base/url_recovery.sqlite3')
            self.cursor_db = self.connect_db.cursor()
                
            function(self)
                
            self.connect_db.commit()
            self.connect_db.close()
                
        return wrapper
    
    
    @staticmethod
    def _decorator_clear_all(function):
        """ Decorator funtion used for complement
        the functions manager of clean the window.
        MODULE: tools.download
        """
            
        def wrapper(self):
            self.URL.set('')
            self.TYPES.set('Types')
            self.RENAME.set('')
            self.PATH_DIR = None
                
            function(self)
                
        return wrapper