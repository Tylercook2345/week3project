print("Welcome to my ROI calculator")
#I'll have to come back to this in the future

class monthlyIncome:
    item = "Monthly Income"
    def __init__(self, rentalincome, salary):
        self.rentalincome = rentalincome
        self.salary = salary
        pass


class expenses:
    item = "Montly Expenses"
    def __init__(self, taxes, propertyinsurance, utilties, repairs, mortgage):
        self.propertyinsurance = propertyinsurance 
        self.taxes = taxes 
        self.utilities = utilties
        self.repairs = repairs
        self.mortgage = mortgage 
        pass

class cashflow: (monthlyIncome-expenses)
item = "Cash Flow"
pass

class cashoncashROI:
    item = "Cash On Cash ROI"
    def __init__(self, downpayment, closingcosts, rehab, misc):
        self.downpayment = downpayment
        self.closingcosts = closingcosts 
        self.rehab = rehab
        self.misc = misc
        pass

