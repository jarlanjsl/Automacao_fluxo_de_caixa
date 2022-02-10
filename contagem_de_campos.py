import xlrd

loc = 'novasEmpresas.xls'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# Extraindo número de linhas
linhas = sheet.nrows - 1
print(f'Numero de linhas na planilha: {linhas}')

# Vericando implementação de celula
"""
l: linhas
c: colunas
"""
l1 = 0
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
    print(f'Linhas restantes: {linhas - 1}')
    print(f'Linha atual: {l1}')
    print(f"Linha {l1} = '{campo_a}','{campo_b}','{campo_c}','{campo_e}','{campo_f}'")
    linhas -= 1
    l1 += 1
    campo_a = sheet.cell_value(l1, ca)
    campo_b = sheet.cell_value(l1, cb)
    campo_c = sheet.cell_value(l1, cc)
    campo_e = sheet.cell_value(l1, ce)
    campo_f = sheet.cell_value(l1, cf)
