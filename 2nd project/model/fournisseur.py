import psycopg2.extras
from model.db import DB

class Fournisseur():

    def __init__(self, db):
        self.db:DB = db

    def list(self, searchKey=None):
        sql = '''SELECT * FROM fournisseur order by nom'''
        with self.db.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql)
            # self.db.connection.commit()
            return cursor.fetchall()
        
    def getById(self, id):
        sql = '''SELECT * FROM fournisseur where id = %s'''
        with self.db.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(sql, (id,))
            # self.db.connection.commit()
            return cursor.fetchone()
        
    def inserer(self, data):
        sql = '''INSERT INTO fournisseur (nom, prenom, num) VALUES (%s,%s,%s)'''
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(sql, data)
                self.db.connection.commit()
                return {'is_ok':True , 'message':''}
        except Exception as e:
            self.db.connection.rollback()
            return {'is_ok':False , 'message':str(e)}
        
    def modifier(self, data):
        sql = '''UPDATE fournisseur set nom = %s, prenom = %s, num = %s where id = %s'''
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(sql, data)
                self.db.connection.commit()
                return {'is_ok':True , 'message':''}
        except Exception as e:
            self.db.connection.rollback()
            return {'is_ok':False , 'message':str(e)}
        
    def supprimer(self, id):
        sql = '''DELETE FROM fournisseur WHERE id = %s'''
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(sql, (id,))
                self.db.connection.commit()
                return {'is_ok': True, 'message': ''}
        except Exception as e:
            self.db.connection.rollback()
            return {'is_ok': False, 'message': str(e)}
