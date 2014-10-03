#!/usr/bin/env python

from xlrd import open_workbook
from paycheck import Paycheck

paycheckWorkbook = open_workbook('sheets/paycheck.xlsx')

def readPaychecks(sheet, columns, rows):
    paychecks = []
    for row in range(1,rows):
        values = []
        for column in range(columns):
            values.append(sheet.cell(row,column).value)
        paychecks.append(Paycheck(*values))

for sheet in paycheckWorkbook.sheets():
    sheetColumns = sheet.ncols
    sheetRows = sheet.nrows 
    print 'Sheet: ',sheet.name
    print '        with ' + str(sheetRows) + ' rows and ' + str(sheetColumns) + ' columns'
    paychecks = readPaychecks(sheet, sheetColumns, sheetRows)


