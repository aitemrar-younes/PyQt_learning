import psycopg2
import psycopg2.extras
from .db import DB

class Item():
    def __init__(self, db):
        self.db:DB = db

    # list item
    def list_item_all(self):
        sql_query = 'select * from item'
        with self.db.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(sql_query)
            return cursor.fetchall()

    # list filtred item
    def list_item_active(self):
        pass

    def list_item_disable(self):
        pass

    def list_item_filterd(self):
        pass
    
    def ajouter_item(self, data):
        sql_insert = 'insert into item (nom, designation) values (%s,%s)'
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(sql_insert, data)
                self.db.connection.commit()
                return {'is_ok':True, 'message':'' }
        except psycopg2.Error as e:
            self.db.connection.rollback()
            return {'is_ok':False, 'message':str(e) }

    
    def modifier_item(self, data_columns, data_values):
        pass
    
    def supprimer_item(self, data_columns, data_values):
        pass
    