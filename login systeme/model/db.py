import psycopg2
import psycopg2.extras

class DB():
    # Setting init variables
    connection = None
    
    # Connection configuration
    host = 'localhost'
    port = 5432
    dbname = 'store'
    user = 'postgres'
    password = 'Test0123*'

    def connect(self, utilisateur, password):
        try:
            self.connection = psycopg2.connect( host=self.host, port=self.port, dbname=self.dbname , user=utilisateur, password=password )
            return True
        except Exception as e:
            print(e)
        return False

    def close(self):
        if not self.connection is None:
            self.connection.close()
        self.connection = None # is it worth it this instruction ****