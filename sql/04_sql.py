import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()

    for r in rows:
        print(r[0], r[1], "\n", r[2])
        cursor.execute("SELECT count(order_date) FROM orders WHERE make=? and model=?",(r[0], r[1]))
        order_count = cursor.fetchone()[0]
        print(order_count)
