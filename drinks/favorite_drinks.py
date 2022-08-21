import sqlite3
import os

try:
	os.remove("drinks.db")
except FileNotFoundError:
	pass

connection = sqlite3.connect("drinks.db")

cur = connection.cursor()

cur.execute("""
	CREATE TABLE people (
		idPerson 						INTEGER PRIMARY KEY,
		firstname 					VARCHAR(64),
		favoriteDrink 			INTEGER
	);
""")

cur.execute("""
	CREATE TABLE drinks (
		idDrink 						INTEGER PRIMARY KEY,
		name 								VARCHAR(64)
	);
""")

cur.execute("""
  INSERT INTO drinks (name) VALUES
		("Wasser"),
		("Sirup"),
		("Cola"),
		("Süssmost"),
		("Rivella"),
		("Eistee"),
		("Bier")
""")

cur.execute("""
  INSERT INTO people (firstname) VALUES
		("Birk"),
		("Micha"),
		("Philipp"),
		("Florian"),
		("Jannis"),
		("Cyril"),
		("Matthew"),
		("Sanchaai"),
		("Rafael");
""")

cur.execute("""UPDATE people SET favoriteDrink = 1 WHERE firstname = 'Micha';""")
cur.execute("""UPDATE people SET favoriteDrink = 2 WHERE firstname = 'Matthew';""")
cur.execute("""UPDATE people SET favoriteDrink = 6 WHERE firstname = 'Philipp';""")

print("cross join")
result = cur.execute("""SELECT firstname, drinks.name FROM people CROSS JOIN drinks;""")
for row in result:
	print(row)

print("inner join")
result = cur.execute("""SELECT firstname, drinks.name FROM people JOIN drinks ON favoriteDrink = idDrink;""")
for row in result:
	print(row)

print("left join")
result = cur.execute("""SELECT firstname, drinks.name FROM people LEFT JOIN drinks ON favoriteDrink = idDrink;""")
for row in result:
	print(row)

### not susported in sqlite3
# print("right join")
# result = cur.execute("""SELECT firstname, drinks.name FROM people RIGHT JOIN drinks ON favoriteDrink = idDrink;""")
# for row in result:
# 	print(row)

print("change tables to emulate RIGTH JOIN")
result = cur.execute("""SELECT firstname, drinks.name FROM drinks LEFT JOIN people ON favoriteDrink = idDrink;""")
for row in result:
	print(row)

### not susported in sqlite3
# print("outer join")
# result = cur.execute("""SELECT firstname, drinks.name FROM people OUTER JOIN drinks ON favoriteDrink = idDrink;""")
# for row in result:
# 	print(row)

print("emulate OUTER JOIN")
result = cur.execute("""SELECT firstname, name FROM 
(
	SELECT firstname, name FROM drinks LEFT JOIN people ON favoriteDrink = idDrink
	UNION ALL 
	SELECT firstname, name FROM people LEFT JOIN drinks ON favoriteDrink = idDrink
);
""")
for row in result:
	print(row)

connection.commit()
connection.close()


