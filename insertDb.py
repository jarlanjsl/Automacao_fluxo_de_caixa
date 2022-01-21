import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_empresas(conn, empresas):
    """
    Create a new project into the projects table
    :param conn:
    :param empresas:
    :return:
    """
    sql = ''' INSERT INTO empresas(id_empresa,descricao,status)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, empresas)
    conn.commit()
    return cur.lastrowid



def main():
    database = r"pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new empresas
        empresas = ('19','JSL','A');
        create_empresas(conn, empresas)


if __name__ == '__main__':
    main()