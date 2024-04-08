"""
0. postgreSQL installation on macos: https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql-macos/
1. pip3 install psycopg2 --break-system-packages
2. Error: pg_config executable not found.
3. here: https://www.geeksforgeeks.org/how-to-fix-pg_config-executable-not-found-in-python
4. pg_config locates at /Library/PostgreSQL/16/bin
5. export PATH=$PATH:/Library/PostgreSQL/16/bin
6. re-run pip3 install psycopg2 --break-system-packages
"""

import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port=5432)
cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     id INT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     gender CHAR       
# );
# """)

# cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
#             (1, 'Mike', 30, 'm'),
#             (2, 'Lisa', 25, 'f'),
#             (3, 'Leo', 40, 'm');
# """)

cur.execute("""
SELECT * FROM person WHERE age <= 30;
""")
for row in cur.fetchall():
    print(row)

sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ("L", 41))
print(sql)
cur.execute(sql)
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()