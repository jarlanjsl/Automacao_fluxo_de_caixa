import xlrd

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

# Extracting number of rows
linhas = sheet.nrows - 1
print(f'Numero de linhas: {linhas}')

# print(values2)
# print(values3)

# Vericando implementação de celula
l1 = 1
ca = 0
campo_a = sheet.cell_value(l1, ca)
print(f'Valor do campo a2: {campo_a}')
cb = 1
campo_b = sheet.cell_value(l1, cb)
print(f'Valor do campo b2: {campo_b}')
cc = 2
campo_c = sheet.cell_value(l1, cc)
print(f'Valor do campo c2: {campo_c}')
ce = 4
campo_e = sheet.cell_value(l1, ce)
print(f'Valor do campo e2: {campo_e}')
cf = 5
campo_f = sheet.cell_value(l1, cf)
print(f'Valor do campo f2: {campo_f}')

while linhas > 0:
    print(f"'{campo_a}','{campo_b}','{campo_c}','{campo_e}','{campo_f}'")
    linhas -= 1
    l1 += 1
    campo_a = sheet.cell_value(l1, ca)
    campo_b = sheet.cell_value(l1, cb)
    campo_c = sheet.cell_value(l1, cc)
    campo_e = sheet.cell_value(l1, ce)
    campo_f = sheet.cell_value(l1, cf)
