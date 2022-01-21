import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_empresas(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM empresas")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_empresas_ativas(conn, status):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM empresas WHERE status=?", (status,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query empresas ativas:")
        select_empresas_ativas(conn, 'A')

        print("2. Query todas empresas")
        select_empresas(conn)


if __name__ == '__main__':
    main()