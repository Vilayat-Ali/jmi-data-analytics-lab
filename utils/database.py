import sqlite3

class Database:
    def __init__(self, db_name: str):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print(f'Database: {db_name} initialized successfully!')
        except sqlite3.Error as error:
            print('Error occurred -', error)

    def run_query(self, query: str, params: tuple = ()):
        try:
            result = self.cursor.execute(query, params)
            self.conn.commit()
            return result
        except sqlite3.Error as error:
            print(f"Failed to run query `{query}` with params `{params}` -", error)
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            print('Database connection closed.')
