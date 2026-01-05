#Variables
employeeName = ""
hoursWorked = 0
rateOfPay = 0.00
taxRate = 0.00

# Get user input
employeeName = input("Enter you name")
hoursWorked = int(input("Enter hours worked"))
rateOfPay = float(input("Enter rate of pay"))
taxRate = float(input("enter tax rate"))


# Calculations
grossPay = hoursWorked * rateOfPay	
taxPaid    = grossPay * taxRate		
nettPay   = grossPay - taxPaid	

#Print emp statement
print("====== EMPLOYEE STATEMENT ======")
print("Employee name:", employeeName)
print("Hours worked", hoursWorked)
print("Rate of pay: $", rateOfPay)
print("Tax rate:", taxRate)
print("Gross pay: $" + str(grossPay))
print("Tax paid: $)", taxPaid)
print("Nett pay $", nettPay)

