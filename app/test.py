import psycopg2

# host: <svc-name>.<ns-name>.svc.cluster.local if the db locates in another ns
# - source: https://medium.com/@SabujJanaCodes/building-a-golang-music-api-and-deploying-it-on-k8s-go-mysql-k8s-841612d13479#:~:text=%3Csvc%2Dname%3E.%3Cns%2Dname%3E.svc.cluster.local
db_params = {
    "host": "postgres.ps-ns.svc.cluster.local", # k get po -n ps-ns -owide, IP column OR k get endpoints -n ps-ns
    "database": "postgres",
    "user": "postgres",
    "password": "pspwd",
    "port": 5432
}

# conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port=5432)
conn = psycopg2.connect(**db_params)
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