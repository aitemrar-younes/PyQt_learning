import psycopg2
import psycopg2.extras
from .db import DB

class Fournisseur():
    def __init__(self, db):
        self.db:DB = db

    # list fournisseur
    def list_fournisseur_all(self):
        sql_query = 'select * from fournisseur'
        with self.db.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql_query)
            return cursor.fetchall()

    # list filtred fournisseur
    def list_fournisseur_active(self):
        pass

    def list_fournisseur_disable(self):
        pass

    def list_fournisseur_filterd(self):
        pass
    
    def ajouter_fournisseur(self, data):
        sql_insert = 'insert into fournisseur (nom, prenom, num, adrress) values (%s,%s,%s,%s)'
        with self.db.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql_insert, data)
            self.db.connection.commit()
    
    def modifier_fournisseur(self, data_columns, data_values):
        pass
    
    def supprimer_fournisseur(self, data_columns, data_values):
        pass
    