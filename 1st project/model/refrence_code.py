import psycopg2
import psycopg2.extras

# Setting init variables
connection = None
cursor = None
# Connection configuration
host = 'localhost'
port = 5432
dbname = 'store'
user = 'postgres'
password = 'Test0123*'

try:
    # Initialise connection
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password,
    )
    # this parametre helps to get data in form of dictionairy
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # implement check for tables

    # if doesnt exists create them
    
    # Create table
    sql_create = ''' create table if not exists fournisseur(
        id SERIAL,
        nom varchar(30),
        prenom varchar(30),
        num varchar(30),
        adrress varchar(150),
        deleted BOOLEAN NOT NULL default 't'
    )'''
    cursor.execute(sql_create)
    connection.commit()
    
    # Insertion
    sql_insert = '''insert into fournisseur (nom, prenom, num, adrress) values (%s,%s,%s,%s)'''
    sql_insert_values = ('aitemrar', 'younes abdenacer', '0799552071', 'Blida boufaril route soummaa')
    cursor.execute(sql_insert, sql_insert_values)
    connection.commit()

except Exception as e:
    print(e)
finally:
    if not cursor is None:
        cursor.close()
    if not connection is None:
        connection.close()