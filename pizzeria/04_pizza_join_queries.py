import sqlite3

connection = sqlite3.connect("pizzeria.db")

cur = connection.cursor()

def show(sqlStatement):
	print("*"*60)
	print(sqlStatement.strip())
	result = cur.execute(sqlStatement)
	for row in result:
		print(row)
	print("\n")

print("-----------\nJOIN ...\n-----------")

print("Welche Pizza hat welche Zutaten")
show("""SELECT pizzalist.name, toppings.name FROM pizzalist
	JOIN toppingsForPizza USING (idPizza)
	JOIN toppings USING (idTopping)
""")

print("Wer bestellte wie viele Pizze?")
show("""SELECT firstname, count(*) FROM customers
	JOIN orders USING (idCustomer)
	JOIN pizzaOrders USING (idOrder)
	GROUP BY idCustomer
""")

print("Wer bestellte welche Zutat wie oft?")
show("""SELECT firstname, toppings.name, count(*) FROM customers
	JOIN orders USING (idCustomer)
	JOIN pizzaOrders USING (idOrder)
	JOIN toppingsForPizza USING (idPizza)
	JOIN toppings USING (idTopping)
	GROUP BY idCustomer, idTopping
""")

print("Wer bestellte welche Zutat am häufigsten?")
show("""SELECT firstname, toppingName, MAX(toppingCount) from
	(SELECT firstname, toppings.name as toppingName, count(*) as toppingCount FROM customers
		JOIN orders USING (idCustomer)
		JOIN pizzaOrders USING (idOrder)
		JOIN toppingsForPizza USING (idPizza)
		JOIN toppings USING (idTopping)
		GROUP BY idCustomer, idTopping
	)
	GROUP BY firstname 
""")
