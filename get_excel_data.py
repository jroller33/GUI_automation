import xlrd

excel_file = xlrd.open_workbook("C:/Users/jtrol/Documents/SCRIPT_OUTPUT/2023-08-21--11-46-31--[YMD-hms].xls")

worksheet = excel_file.sheet_by_index(0)

# first_payday = worksheet.cell_value(19,0)

# second_payday = worksheet.cell_value(20,0)

# print(f"On {first_payday} MAnn was paid {worksheet.cell_value()}")

# print(worksheet.cell_value(19,23))

# print(f"cols: {worksheet.ncols} \n rows: {worksheet.nrows}")