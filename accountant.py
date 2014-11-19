from paycheck import PaycheckReceipt,PaycheckReceived

class BankTransferError(Exception):
    def __init__(self,irregular_transfers):
        self.irregular_transfers = irregular_transfers

    def __str__(self):
        return '\n'.join([' For %s I was expecting %s eur and got %s eur' % (irregular_transfer[0],
                                                                  irregular_transfer[1],
                                                                  irregular_transfer[2])
               for irregular_transfer in self.irregular_transfers])

#TODO put these in an Account class
def read_paychecks_received(sheet, columns, rows):
    paychecks = []
    for row in range(1,rows):
        values = []
        for column in range(columns):
            value = sheet.cell(row,column).value
            if value != '':
                values.append(value)
            else:
                values.append(0)
        values = [float(value) for value in values]
        paycheck = PaycheckReceived(*values)
        paychecks.append(paycheck)
    return paychecks

def read_paycheck_receipts(sheet, columns, rows):
    paychecks = []
    for row in range(1,rows):
        values = []
        for column in range(columns):
            value = sheet.cell(row,column).value
            if value != '':
                values.append(value)
            else:
                values.append(0)
        values = [float(value) for value in values]
        paycheck = PaycheckReceipt(*values)
        paychecks.append(paycheck)
    return paychecks

def check_bank_transfers(receipts,received):
    receipt_dict = dict(('_'.join([str(receipt.year),str(receipt.month)]),
                                  receipt.liquid_total) 
                         for receipt in receipts)
    received_dict = {}
    for received_transfer in received:
        key = '_'.join([str(received_transfer.year),
                        str(received_transfer.month)])
        try:
            received_dict[key] += received_transfer.received
        except KeyError:
            received_dict[key] = received_transfer.received

    irregular_transfers = []
    for month in received_dict.keys():
        if abs((receipt_dict[month] - received_dict[month])) > 0.01:
            irregular_transfers.append((month,receipt_dict[month],received_dict[month]))

    if irregular_transfers:
        total_irregular_receipts = sum([irregular_transfer[1] for irregular_transfer in irregular_transfers])
        total_irregularly_received = sum([irregular_transfer[2] for irregular_transfer in irregular_transfers])
        print ' We are missing %s euros... ' % (total_irregular_receipts - total_irregularly_received)
        raise BankTransferError(irregular_transfers)


def calculate_subsidy
