import sqlite3
from random import randint

connection = sqlite3.connect("pizzeria.db")

cur = connection.cursor()

cur.execute("""DELETE FROM orders WHERE true;""")
cur.execute("""DELETE FROM pizzaOrders WHERE true;""")

users = cur.execute("SELECT idCustomer FROM customers").fetchall()
pizzaIds = cur.execute("SELECT idCustomer FROM customers").fetchall()
lastPizza = pizzaIds[-1][0]
print(lastPizza)

for row in users:
	id = row[0]
	for order in range(randint(0, 10)):
		idOrder = cur.execute("INSERT INTO orders (idCustomer) VALUES (?) RETURNING idOrder", (id,)).fetchone()[0]
		pizzaOrders = [0] * (lastPizza + 1)
		for n in range(randint(1, 10)):
			randomId = randint(1, lastPizza)
			pizzaOrders[randomId] += 1
		for idPizza, amount in enumerate(pizzaOrders):
			if amount > 0:
				cur.execute("""INSERT INTO pizzaOrders (idOrder, idPizza, amount) VALUES (?, ?, ?)""", (idOrder, idPizza, amount))

cur.execute("""UPDATE orders SET paid = CURRENT_TIMESTAMP WHERE idOrder = 1""")
cur.execute("""UPDATE orders SET delivered = CURRENT_TIMESTAMP WHERE idOrder = 2""")
cur.execute("""UPDATE orders SET paid = CURRENT_TIMESTAMP, delivered = CURRENT_TIMESTAMP WHERE idOrder = 3""")

result = cur.execute("""SELECT * FROM orders WHERE idOrder < 5""")
for row in result:
	print(row)


cur.execute("""DELETE from orders WHERE paid AND delivered""")

result = cur.execute("""SELECT * FROM orders WHERE idOrder < 5""")
for row in result:
	print(row)


connection.commit()
connection.close()
