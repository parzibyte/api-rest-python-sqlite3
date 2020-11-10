import sqlite3
DATABASE_NAME = "games.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
				price REAL NOT NULL,
				rate INTEGER NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
