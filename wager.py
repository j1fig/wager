from xlrd import open_workbook
from person import Person
from bill import Bill
from datetime import date, timedelta

billWorkbook = open_workbook('../bills.xls')

def readPeople(sheet, columns, rows):
    people = []
    for column in range(columns):
        values = []
        for row in range(rows):
            values.append(sheet.cell(row,column).value)
        if values[0] == 'Name':
            print 'Ignoring column...'
            continue
        people += [Person(values[0])]
    return people

def readBills(sheet, columns, rows):
    bills = []
    for column in range(columns):
        values = []
        for row in range(rows):
            values.append(sheet.cell(row,column).value)
        if values[0] == 'Name':
            print 'Ignoring column...'
            continue
        bills += [Bill(values[0],values[1],values[2],values[3],values[4],values[5])]
    return bills

def calculateMonthlyExpenses(bills, people):
    monthBillStarts = [ bill.start.month for bill in bills]
    monthBillEnds = [ bill.end.month for bill in bills]
    monthsWithBills = [ (str(month),MonthlyExpense(month)) for month in monthBillStarts]
    if monthBillEnds[-1] not in monthBillStarts:
      monthsWithBills += [monthBillEnds[-1]]
    monthlyExpenses = dict(monthsWithBills)
    for bill in bills:
        monthlyExpenses[str(bill.start.month)] = MonthlyExpense(bill.start)

def calculateDebts(bills, people):
    
    

for sheet in billWorkbook.sheets():
    sheetColumns = sheet.ncols
    sheetRows = sheet.nrows 
    print 'Sheet: ',sheet.name
    print '        with ' + str(sheetRows) + ' rows and ' + str(sheetColumns) + ' columns'
    if sheet.name == 'Bills':
        the_bills = readBills(sheet, sheetColumns, sheetRows)
    elif sheet.name == 'People':
        the_people = readPeople()


debts = calculateDebts(the_bills, the_people)

print debts
