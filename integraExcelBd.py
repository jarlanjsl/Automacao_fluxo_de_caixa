import xlrd
import sqlite3
from sqlite3 import Error

loc = 'novasEmpresas.xls'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# Valores
a2 = sheet.cell_value(1, 0)
b2 = sheet.cell_value(1, 1)
c2 = sheet.cell_value(1, 2)
# d2 = sheet.cell_value(1, 3)
e2 = sheet.cell_value(1, 4)
f2 = sheet.cell_value(1, 5)

a3 = sheet.cell_value(2, 0)
b3 = sheet.cell_value(2, 1)
c3 = sheet.cell_value(2, 2)
# d3 = sheet.cell_value(2, 3)
e3 = sheet.cell_value(2, 4)
f3 = sheet.cell_value(2, 5)

# Expressão de insert
values2 = f"'{a2}','{b2}','{c2}','{e2}','{f2}'"
values3 = f"'{a3}','{b3}','{c3}','{e3}','{f3}'"


#print(values2)
#print(values3)

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
    sql = ''' INSERT INTO empresas(id_empresa,descricao,usuario_criador,dt_criacao,status)
              VALUES(?,?,?,?,?) '''
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
        print(values3)
        empresas = (f'{a3}',f'{b3}',f'{c3}',f'{e3}',f'{f3}');
        create_empresas(conn, empresas)


if __name__ == '__main__':
    main()

