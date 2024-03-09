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

    def __init__(self):
        self.connect()

    def connect(self):
        try:
            self.connection = psycopg2.connect( host=self.host, port=self.port, dbname=self.dbname , user=self.user, password=self.password )
        except Exception as e:
            print(e)

    def close(self):
        if not self.connection is None:
            self.connection.close()
            self.connection = None # is it worth it this instruction ****

    # this will help user to know if there is missing tables and if he want to create them by pressing yes
    # basically what it does it do select on all tables
    def checkMissingTables(self):
        try:
            sql_query = 'select * from fournisseur'
            with self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(sql_query)
        except:
            return {'status':'error', 'message':'No table fournisseur'}
        return {'status':'ok', 'message':'table fournisseur is present'}
    
    def createTablesIfNotExists(self):
        # Create table
        sql_create = ''' create table if not exists fournisseur(
            id SERIAL,
            nom varchar(30),
            prenom varchar(30),
            num varchar(30),
            adrress varchar(150),
            deleted BOOLEAN NOT NULL default 't'
        )'''
        with self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql_create)

    # insert default record like brand of cars that are considered as a constant
    def settingDefaultRecordsForTables(self):
        sql_insert = '''insert into fournisseur (nom, prenom, num, adrress) values (%s,%s,%s,%s)'''
        sql_insert_values = ('aitemrar', 'younes abdenacer', '0799552071', 'Blida boufaril route soummaa')
        with self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql_insert, sql_insert_values)