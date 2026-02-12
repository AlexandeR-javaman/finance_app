import sqlite3

from repositories.finance_repository import FinanceRepository


class SQLiteFinanceRepository(FinanceRepository):
    def __init__(self, db_name='finance.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS finance (
                id INTEGER PRIMARY KEY,
                description TEXT,
                costs TEXT,
                total REAL
            )
        ''')
        self.conn.commit()

    def add(self, description, costs, total):
        self.cursor.execute(
            'INSERT INTO finance(description, costs, total) VALUES (?, ?, ?)',
            (description, costs, total)
        )
        self.conn.commit()

    def update(self, record_id, description, costs, total):
        self.cursor.execute(
            'UPDATE finance SET description=?, costs=?, total=? WHERE id=?',
            (description, costs, total, record_id)
        )
        self.conn.commit()

    def delete(self, record_id):
        self.cursor.execute('DELETE FROM finance WHERE id=?', (record_id,))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute('SELECT * FROM finance')
        return self.cursor.fetchall()
