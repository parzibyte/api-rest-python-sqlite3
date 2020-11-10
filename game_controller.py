from db import get_db


def insert_game(name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO games(name, price, rate) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, price, rate])
    db.commit()
    return True


def update_game(id, name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE games SET name = ?, price = ?, rate = ? WHERE id = ?"
    cursor.execute(statement, [name, price, rate, id])
    db.commit()
    return True


def delete_game(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, price, rate FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_games():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, price, rate FROM games"
    cursor.execute(query)
    return cursor.fetchall()
