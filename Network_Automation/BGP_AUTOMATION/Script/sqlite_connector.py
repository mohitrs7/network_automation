import sqlite3
import datetime


class DatabaseConnections():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    ##############################################################
    # This method connects DB to python application
    # returns :
    #              global connection object
    #              cursor object
    # Usage :
    #     self._connectDb()
    ##############################################################
    def _connectDb(self):
        try:
            self.sqliteConnection = sqlite3.connect('transaction.db',
                                                    detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
            self.cursor = self.sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    ##############################################################
    # This method close DB connection.
    # returns : NA
    # Usage :
    #     self._dbConnClose()
    ##############################################################
    def _dbConnClose(self):
        if self.sqliteConnection:
            self.cursor.close()
            self.sqliteConnection.close()
            print("The SQLite connection is closed")

    ##############################################################
    # This method creates DB table
    # attributes :NA
    # Usage :
    #     self._createDatabaseTable()
    ##############################################################
    def _createDatabaseTable(self):
        create_transection_table="""
           CREATE TABLE if not exists Transection_record (
           run_id INTEGER PRIMARY KEY AUTOINCREMENT,
           start_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, 
           end_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        );
        """
        self.cursor.execute(create_transection_table)

    ##############################################################
    # This method creates the router interface based on provided input
    # attributes :
    #              start_timestamp :Start time for program run
    #              end_timestamp :  End time for program run
    # Usage :
    #     self._update_DatabaseTable(start_timestamp, end_timestamp)
    ##############################################################
    def _update_DatabaseTable(self, start_timestamp, end_timestamp):
        update_records = """
        INSERT INTO Transection_record 
        (start_timestamp, end_timestamp) 
        VALUES
        (?,?)
        """
        data_tuple = (start_timestamp, end_timestamp)
        self.cursor.execute(update_records, data_tuple)
        self.sqliteConnection.commit()

    ##############################################################
    # This method shows total run time based out of start and end time
    # attributes :
    #              NA
    # Usage :
    #     self._getRunDetail()
    ##############################################################
    def _getRunDetail(self):
        get_detail = """
        select  ROUND(start_timestamp,2) , ROUND(end_timestamp,2)  from Transection_record 
        where run_id = ? 
        """
        self.cursor.execute(get_detail, (1,))
        records = self.cursor.fetchall()
        for row in records:
            start_timestamp = row[0]
            end_timestamp = row[1]
            print(f"start time is {start_timestamp}")
            print(f"End time is {end_timestamp}")

