
class PaycheckReceipt:
    def __init__(self,*args,**kwargs):
        self.year = int(args[0])
        self.month = int(args[1])
        self.pay = args[2]
        self.vacation_subsidy = args[3]
        self.christmas_subsidy = args[4]
        self.irs = args[5]
        self.irs_on_vacation_subsidy = args[6]
        self.irs_on_christmas_subsidy = args[7]
        self.social_security = args[8]
        self.pay_on_vacation = args[9]
        self.overtax = args[10]
        self.overtax_on_vacation_subsidy = args[11]
        self.overtax_on_christmas_subsidy = args[12]
        self.meal_subsidy_tax_exempt = args[13] + args[14]
        self.meal_subsidy_non_tax_exempt = args[16]
        self.on_travel_pay = args[17]
        self.liquid_total = self.calculate_liquid_total()

    def calculate_liquid_total(self):
        return self.pay + \
               self.vacation_subsidy + \
               self.christmas_subsidy + \
               self.irs + \
               self.irs_on_vacation_subsidy + \
               self.irs_on_christmas_subsidy + \
               self.social_security + \
               self.pay_on_vacation + \
               self.overtax + \
               self.overtax_on_vacation_subsidy + \
               self.overtax_on_christmas_subsidy + \
               self.on_travel_pay
        
    def __str__(self):
        return ' Paycheck receipt in %s of %s, totalling %s. ' %(self.year,
                                                                  self.month,
                                                                  self.liquid_total)

class PaycheckReceived:
    def __init__(self,*args,**kwargs):
            self.year = int(args[0])
            self.month = int(args[1])
            self.received = args[2]

    def __add__(self,other):
        self.received += other.received

    def __str__(self):
        return ' Paycheck received in %s of %s, totalling %s. ' %(self.year,
                                                                  self.month,
                                                                  self.received)
