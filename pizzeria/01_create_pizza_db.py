import sqlite3
import os

try:
	os.remove("pizzeria.db")
except FileNotFoundError:
	pass

connection = sqlite3.connect("pizzeria.db")

cur = connection.cursor()

cur.execute("""
	CREATE TABLE pizzalist (
		idPizza		INTEGER PRIMARY KEY,
		name		VARCHAR(64),
		price		DECIMAL(5, 2)
	);
""")

cur.execute("""
	CREATE TABLE IF NOT EXISTS toppings (
		idTopping	INTEGER PRIMARY KEY,
		name		VARCHAR(64),
		vegan		BOOLEAN
	);
""")

cur.execute("""
	INSERT INTO pizzalist (name, price) VALUES
		('Margerita', 12.00),
		('Prosciutto', 15.00),
		('Prosciutto e funghi', 16.00),
		('Funghi', 14.00),
		('Marinara', 12.00),
		('Diavolo', 16.00)
	;   
""")

cur.execute("""
	INSERT INTO toppings (name, vegan) VALUES
		('pomodoro', true),
		('mozzarella', false),
		('prosciutto', false),
		('funghi', true),
		('aglio', true),
		('peperoncini', true)
	;   
""")

cur.execute("""
	CREATE TABLE toppingsForPizza (
		idPizza			INTEGER,
		idTopping		INTEGER,
		PRIMARY KEY (idPizza, idTopping)
	);
""")

cur.execute("""
	INSERT INTO toppingsForPizza (idPizza, idTopping) VALUES
		(1,1), (1,2),
		(2,1), (2,2), (2,3),
		(3,1), (3,2), (3,3), (3,4),
		(4,1), (4,2), (4,4),
		(5,1), (5,4),
		(6,1), (6,2), (6,3), (6,5), (6,6)
	;
""")

cur.execute("""
	CREATE TABLE customers (
		idCustomer	INTEGER PRIMARY KEY,
		firstname	TEXT
	);
""")

cur.execute("""
	INSERT INTO customers (firstname) VALUES
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

cur.execute("""
	CREATE TABLE orders (
		idOrder		INTEGER PRIMARY KEY,
		idCustomer	INTEGER,
		orderdate	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		paid		TIMESTAMP DEFAULT NULL,
		delivered	TIMESTAMP DEFAULT NULL
	);
""")

cur.execute("""
	CREATE TABLE pizzaOrders (
		idOrder		INTEGER,
		idPizza		INTEGER,
		amount		INTEGER,
		PRIMARY KEY (idOrder, idPizza)
	);
""")

connection.commit()
connection.close()
