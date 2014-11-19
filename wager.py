#!/usr/bin/env python

from xlrd import open_workbook
import accountant

paycheckWorkbook = open_workbook('sheets/paycheck.xlsx')

receipt_sheet = paycheckWorkbook.sheet_by_name('Recibo')
received_sheet = paycheckWorkbook.sheet_by_name('Recebido')
sheetColumns = receipt_sheet.ncols
sheetRows = receipt_sheet.nrows 

#TODO pass only a list, without need to pass rows and columns

paycheck_receipts = accountant.read_paycheck_receipts(receipt_sheet, 
                                         sheetColumns, 
                                         sheetRows)
sheetColumns = received_sheet.ncols
sheetRows = received_sheet.nrows 
paychecks_received = accountant.read_paychecks_received(received_sheet, 
                                 sheetColumns, 
                                 sheetRows)

for paycheck_receipt in paycheck_receipts:
    print paycheck_receipt
for paycheck_received in paychecks_received:
    print paycheck_received


try:
    accountant.check_bank_transfers(paycheck_receipts,paychecks_received)
except accountant.BankTransferError as e:
    print e

