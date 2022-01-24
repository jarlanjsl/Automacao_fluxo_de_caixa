import xlrd
import sqlite3
from sqlite3 import Error

loc = 'novasEmpresas.xls'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)


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


loc = 'novasEmpresas.xls'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# Extraindo número de linhas
linhas = sheet.nrows - 1
print(f'Numero de linhas: {linhas}')

# Vericando implementação de celula
l1 = 1
ca = 0
cb = 1
cc = 2
ce = 4
cf = 5
campo_a = sheet.cell_value(l1, ca)
campo_b = sheet.cell_value(l1, cb)
campo_c = sheet.cell_value(l1, cc)
campo_e = sheet.cell_value(l1, ce)
campo_f = sheet.cell_value(l1, cf)

while linhas > 0:
    print(f"'{campo_a}','{campo_b}','{campo_c}','{campo_e}','{campo_f}'")
    linhas -= 1
    l1 += 1
    campo_a = sheet.cell_value(l1, ca)
    campo_b = sheet.cell_value(l1, cb)
    campo_c = sheet.cell_value(l1, cc)
    campo_e = sheet.cell_value(l1, ce)
    campo_f = sheet.cell_value(l1, cf)


    def main():
        database = r"pythonsqlite.db"

        # create a database connection
        conn = create_connection(database)
        with conn:
            # create a new empresas
            empresas = (campo_a, campo_b, campo_c, campo_e, campo_f)
            create_empresas(conn, empresas)


    if __name__ == '__main__':
        main()
