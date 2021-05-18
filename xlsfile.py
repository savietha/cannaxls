# Program extracting first column
import xlrd
import pandas as pd

df1= pd.read_excel (r'C:/Users/hp/Desktop/assign1/CANNA Product Item detail.xls')
df = pd.DataFrame(df1)
print(df)

loc = ("C:/Users/hp/Desktop/assign1/CANNA Product Item detail.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
	print(sheet.cell_value(i, 1))
