import psycopg2

class DB():
    connection = None
    def __init__(self):
        pass

    def connect(self):
        host = 'localhost'
        port = 5432
        db = 'db_2'
        user = 'postgres'
        password = 'Test0123*'
        try:
            self.connection = psycopg2.connect( host=host, port=port, dbname=db, user=user, password=password )
            return {'is_ok' : True, 'message':''}
        except Exception as e:
            return {'is_ok' : False, 'message':str(e)}
        
    def close(self):
        if self.connection is not None:
            self.connection.close()