import sqlite3

con = sqlite3.connect('ures.db')
cursor = con.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        first_name text,
        last_name text,
        phone_num text
    );
'''

cursor.execute(create_table_query)
con.commit()
con.close()


sample_data_query = '''
    INSERT INTO ures(id, first_name, last_name, phone_num)
    VALUES(?, ?, ?, ?)
'''

sample_data = [(8569, 'ashley', 'abd', '0914'),
               (567, 'john', 'cca', '0914'),
               (987, 'sara', 'hhb', '0914')
               ]
# UNIQUE error for same data!

# with sqlite3.connect('ures.db') as con:
#     cursor = con.cursor()
#     cursor.executemany(sample_data_query, sample_data)
# execute -> only one group of data // executemany -> more than one

fetch_data_query = '''
    SELECT id, first_name, last_name, phone_num FROM users 
'''  # wat??!
rows = []
with sqlite3.connect('ures.db') as con:
    cursor = con.cursor()
    cursor.execute(fetch_data_query)
    rows = cursor.fetchall()

for row in rows:
    print(f'id: {row[0]}, FN: {row[1]}, LN: {row[2]}, PHN: {row[3]}')

