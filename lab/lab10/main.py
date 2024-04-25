import psycopg2
conn= psycopg2.connect(host="localhost", dbname="Nurtay", user="postgres",
                       password="kaziev2004", port="5432")
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS person(
   id INT PRIMARY KEY,
   name VARCHAR(255),
   phone INT,
   gender CHAR);
   """)
cur.execute("""INSERT INTO person (id, name, phone, gender) VALUES
            (1, 'Mike', 8747179, 'm'),
            (2, 'ajsjs', 8747179, 'm'),
            (3, 'Diaskojsaoi', 8707900, 'f')""")
# cur.execute("""SELECT * FROM person WHERE gender = 'm'; """)
# print(cur.fetchone())
conn.commit()
cur.close()
conn.close()