class Paycheck:
    def __init__(self,*args,**kwargs):
            self.year = args[0]
            self.month = args[1]
            self.pay = args[2]
            self.vacation_subsidy = args[3]
            self.christmas_subsidy = args[4]
            self.irs = args[5]
            self.irs_on_vacation_subsidy = args[5]
            self.irs_on_christmas_subsidy = args[6]
            self.social_security = args[7]
            self.pay_on_vacation = args[8]
            self.overtax = args[9]
            self.overtax_on_vacation_subsidy = args[10]
            self.overtax_on_christmas_subsidy = args[11]
            self.meal_subsidy_tax_exempt = args[12]
            self.meal_subsidy_non_tax_exempt = args[13]
            self.on_travel_pay = args[14]

