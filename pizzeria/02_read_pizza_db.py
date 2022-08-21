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

print("READ PIZZA LIST")

result = cur.execute("""SELECT * FROM pizzalist;""")
for row in result:
	print(row)


print("READ CUSTOMERS")
show("""SELECT * FROM customers;""")


print("READ SELECTED COLUMNS FROM TOPPINGS")
show("""SELECT name, vegan FROM toppings;""")

print("-----------\nWHERE ...\n-----------")

print("READ CHEAPEST ITEM")
show("""SELECT name, price FROM pizzalist WHERE price < 15;""")

print("GET PIZZA BY NAME")
show("""SELECT name, price FROM pizzalist WHERE name = 'Funghi';""")

print("GET PIZZA BY NAME WITH WILDCARDS")
show("""SELECT name, price FROM pizzalist WHERE name LIKE '%ar%';""")

print("MULTIPLE CONDITIONS")
show("""SELECT name, price FROM pizzalist WHERE name LIKE 'M%' or name LIKE 'P%';""")

print("READ TOPPINGS WITH WHERE CLAUSE")
show("""SELECT name, vegan FROM toppings WHERE vegan = true;""")

print("-----------\nORDER BY ...\n-----------")

print("ORDER BY PRICE")
show("""SELECT name, price FROM pizzalist ORDER BY price ASC""")

print("ORDER BY NAME")
show("""SELECT name, price FROM pizzalist ORDER BY name""")

print("-----------\nOPERATIONS\n-----------")

print("MIN, MAX")
show("""SELECT 'Salsa' as 'Lokal', MIN(PRICE), MAX(PRICE) FROM pizzalist;""")

print("AVG, SUM, COUNT")

show("""SELECT SUM(price), COUNT(*), AVG(price) FROM pizzalist;""")

print("-----------\nJOIN ...\n-----------")

print("JOIN")
show("""SELECT pizzalist.name, toppings.name FROM pizzalist
	JOIN toppingsForPizza USING (idPizza)
	JOIN toppings USING (idTopping)
""")