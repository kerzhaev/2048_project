import sqlite3

bd = sqlite3.connect('2048.sqlite')

cur = bd.cursor()

cur.execute('''
create table if not exists RECORDS (
        name text,
        score integer
)''')
cur.execute('''
SELECT name, max(score) score from RECORDS
GROUP by name
ORDER by score DESC
LIMIT 3
''')

result = cur.fetchall()


cur.close()