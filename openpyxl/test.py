from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet() # insert at the end (default)
ws.title = "New Title 1 asdasddsasdf"
c = ws['A4']
c.value = 'hello, world'
wb.save('balances.xlsx')
print "Worked?"