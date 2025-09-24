import sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("billing.db")
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT
        )""")
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        )""")
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            total REAL,
            FOREIGN KEY(customer_id) REFERENCES customers(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        )""")
        self.conn.commit()

    def add_customer(self, name, contact):
        self.conn.execute("INSERT INTO customers (name, contact) VALUES (?, ?)", (name, contact))
        self.conn.commit()

    def add_product(self, name, price):
        self.conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def add_transaction(self, customer_id, product_id, quantity, total):
        self.conn.execute("INSERT INTO transactions (customer_id, product_id, quantity, total) VALUES (?, ?, ?, ?)",
                          (customer_id, product_id, quantity, total))
        self.conn.commit()

    def get_customers(self):
        return self.conn.execute("SELECT * FROM customers").fetchall()

    def get_products(self):
        return self.conn.execute("SELECT * FROM products").fetchall()

