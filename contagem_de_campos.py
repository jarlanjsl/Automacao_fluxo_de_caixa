import xlrd

loc = 'orcado.xls'

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
cd = 3
cf = 5
ch = 7
cj = 9
ck = 10
cm = 12
cn = 13
campo_a = sheet.cell_value(l1, ca)
campo_b = sheet.cell_value(l1, cb)
campo_c = sheet.cell_value(l1, cc)
campo_d = sheet.cell_value(l1, cd)
campo_f = sheet.cell_value(l1, cf)
campo_h = sheet.cell_value(l1, ch)
campo_j = sheet.cell_value(l1, cj)
campo_k = sheet.cell_value(l1, ck)
campo_m = sheet.cell_value(l1, cm)
campo_n = sheet.cell_value(l1, cn)

while linhas > 0:
    print(f'Linhas restantes: {linhas - 1}')
    print(f'Linha atual: {l1}')
    print(f"Linha {l1} = '{campo_a}','{campo_b}','{campo_c}','{campo_d}','{campo_f}','{campo_h}','{campo_j}','{campo_k},'{campo_m},'{campo_n}'")
    linhas -= 1
    l1 += 1
    campo_a = sheet.cell_value(l1, ca)
    campo_b = sheet.cell_value(l1, cb)
    campo_c = sheet.cell_value(l1, cc)
    campo_d = sheet.cell_value(l1, cd)
    campo_f = sheet.cell_value(l1, cf)
    campo_h = sheet.cell_value(l1, ch)
    campo_j = sheet.cell_value(l1, cj)
    campo_k = sheet.cell_value(l1, ck)
    campo_m = sheet.cell_value(l1, cm)
    campo_n = sheet.cell_value(l1, cn)
