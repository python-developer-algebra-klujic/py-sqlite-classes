import sqlite3

from .models import Cake


# Create table
sql_create_table = '''
CREATE TABLE IF NOT EXISTS cakes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL,
    weight REAL
)
'''

def create_table():
    conn = sqlite3.connect('cakes_db.sqlite')
    cursor = conn.cursor()

    cursor.execute(sql_create_table)
    conn.commit()

    conn.close()



# Insert into table
insert_sql = '''
INSERT INTO cakes (name, price, weight)
VALUES (?, ?, ?)
'''

def insert_into(cake: Cake):
    conn = sqlite3.connect('cakes_db.sqlite')
    cursor = conn.cursor()

    parameters = (cake.name, cake.price, cake.weight)

    cursor.execute(insert_sql, parameters)
    conn.commit()

    conn.close()




# Get all from table
get_sql = '''
SELECT * FROM cakes
'''

def get_cakes():
    conn = sqlite3.connect('cakes_db.sqlite')
    cursor = conn.cursor()

    cursor.execute(get_sql)
    cakes = cursor.fetchall()
    conn.close()

    # Zato sto je svaki element liste s podacima iz baze tipa tuple,
    # moramo ga konvertirati u objekt klase Cake
    return list(map(lambda cake: Cake(cake[1], cake[2], cake[3]), cakes))


# Get one from table
get_sql_by_id = '''
SELECT * FROM cakes WHERE id = ?
'''

def get_cake_by_id(id: int):
    conn = sqlite3.connect('cakes_db.sqlite')
    cursor = conn.cursor()

    cursor.execute(get_sql_by_id, (id,))
    cake = cursor.fetchone()
    conn.close()

    # Zato sto je svaki element liste s podacima iz baze tipa tuple,
    # moramo ga konvertirati u objekt klase Cake
    return Cake(cake[1], cake[2], cake[3])

