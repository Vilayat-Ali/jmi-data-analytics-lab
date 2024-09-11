import sqlite3
from collections import defaultdict
from utils.database import Database
from .contants import products, sales, sales_items

generate_product_table_query = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT NULL,
    price REAL NOT NULL
);
'''

generate_sales_table_query = '''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_date DATE  NOT NULL
);
'''

generate_sales_item_table_query = '''
CREATE TABLE IF NOT EXISTS sales_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sales_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (sales_id) REFERENCES sales(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
'''

def setup_database(db):
    init_table_queries = [
        generate_product_table_query,
        generate_sales_table_query,
        generate_sales_item_table_query
    ]
    
    # Generate a new database with dummy transaction data
    for query in init_table_queries:
        try:
            result = db.run_query(query)
            print(result)
        except Exception as e:
            print(f"Error running query: {e}")

    # Inserting products data
    for product in products:
        try:
            result = db.cursor.execute('''
                INSERT INTO products (name, description, price) VALUES (?, ?, ?);
            ''', product)
            db.conn.commit()
        except Exception as e:
            print(f"Error inserting product {product}: {e}")

    # Inserting sales data
    for sale in sales:
        try:
            result = db.cursor.execute('''
                INSERT INTO sales (transaction_date) VALUES (?);
            ''', sale)
            db.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting sale {sale}: {e}")

    # Inserting sales_items
    for sale_item in sales_items:
        try:
            result = db.cursor.execute('''
                INSERT INTO sales_items (sales_id, product_id, quantity) VALUES (?, ?, ?);
            ''', sale_item)
            db.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting sales item {sale_item}: {e}")


def fetch_data(db):
    db.cursor.execute('''
    SELECT s.id AS sales_id, p.name AS product_name
    FROM sales s
    JOIN sales_items si ON s.id = si.sales_id
    JOIN products p ON si.product_id = p.id
    ORDER BY s.id;
    ''')

    rows = db.cursor.fetchall()

    transactions = defaultdict(list)

    for sales_id, product_name in rows:
        transactions[sales_id].append(product_name)

    transaction_list = list(transactions.values())

    db.conn.close()

    return transaction_list
