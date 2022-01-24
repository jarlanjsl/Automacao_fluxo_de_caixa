import xlrd

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
    print(f'linhas: {linhas}')
    print(f'l1: {l1}')
    linhas -= 1
    l1 += 1
    campo_a = sheet.cell_value(l1, ca)
    campo_b = sheet.cell_value(l1, cb)
    campo_c = sheet.cell_value(l1, cc)
    campo_e = sheet.cell_value(l1, ce)
    campo_f = sheet.cell_value(l1, cf)
