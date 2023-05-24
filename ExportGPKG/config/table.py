from osgeo import gdal



class Table(object):
    """
        Object to save information about tables

    Args:

    """
    def __init__(self, host, port, database, user,password,tablename) -> None:
        """Create a table object

        Args:
            host (string): _description_
            port (string): _description_
            database (string): _description_
            user (string): _description_
            password (string): _description_
            tablename(string): _description_
        """

        self.dbhost=host
        self.dbport=port
        self.dbname=database
        self.username=user
        self.password=password
        self.tablename=tablename

    def __str__(self):
        return f'Table {self.tablename} on IP: {self.dbhost}:{self.dbport} in database name: {self.dbname} and table name: {self.tablename}'
    def __connect__(self):
        return f'"dbname={self.dbname} host={self.dbhost} port={self.dbport} user={self.username} password={self.password}"'

def importTB():
    """Function to import table
    """
    pass
