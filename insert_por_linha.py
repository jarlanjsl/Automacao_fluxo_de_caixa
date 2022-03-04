import xlrd
import sqlite3
from sqlite3 import Error

loc = 'orcado.xls'

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
    sql = ''' INSERT INTO movimentacao(id_mov, id_empresa, descricao, id_conta, id_fornecedor, dt_documento, dt_vencimento, valor_orcado, usuario_criador, status)
              VALUES(((SELECT CAST((SELECT MAX(ID_MOV) FROM movimentacao) AS int)) + 1),?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, empresas)
    conn.commit()
    return cur.lastrowid


loc = 'orcado.xls'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# Extraindo número de linhas
# Linhas - 3 para tirar o cabeçalho, linha de espaçamento e linha final que contém um espaço
linhas = sheet.nrows - 3
print(f'Numero de linhas: {linhas}')

# Vericando implementação de celula
l1 = 1
ca = 0
cb = 1
cc = 2
ce = 4
cg = 6
ci = 8
ck = 10
cl = 11
cm = 12

campo_a = sheet.cell_value(l1, ca)
campo_b = sheet.cell_value(l1, cb)
campo_c = sheet.cell_value(l1, cc)
campo_e = sheet.cell_value(l1, ce)
campo_g = sheet.cell_value(l1, cg)
campo_i = sheet.cell_value(l1, ci)
campo_k = sheet.cell_value(l1, ck)
campo_l = sheet.cell_value(l1, cl)
campo_m = sheet.cell_value(l1, cm)


while linhas > 0:
    print(
        f"Linha {l1} = '{campo_b}','{campo_c}','{campo_e}','{campo_g}','{campo_i}','{campo_k}','{campo_l},'{campo_m}'")
    linhas -= 1
    l1 += 1
    campo_a = sheet.cell_value(l1, ca)
    campo_b = sheet.cell_value(l1, cb)
    campo_c = sheet.cell_value(l1, cc)
    campo_e = sheet.cell_value(l1, ce)
    campo_g = sheet.cell_value(l1, cg)
    campo_i = sheet.cell_value(l1, ci)
    campo_k = sheet.cell_value(l1, ck)
    campo_l = sheet.cell_value(l1, cl)
    campo_m = sheet.cell_value(l1, cm)


    def main():
        database = r"pythonsqlite.db"

        # create a database connection
        conn = create_connection(database)
        with conn:
            # create a new empresas
            empresas = (campo_a, campo_b, campo_c, campo_e, campo_g, campo_i, campo_k, campo_l, campo_m)
            create_empresas(conn, empresas)


    if __name__ == '__main__':
        main()
