#Variables
employeeName = ""
hoursWorked = 0
rateOfPay = 0.00
taxRate = 0.00

# Get user input
employeeName = input("Enter you name")
hoursWorked = int(input("Enter hours worked"))
rateOfPay = float(input("Enter rate of pay"))
taxRate = float(input("enter tax rate")) / 100


# Calculations
grossPay = hoursWorked * rateOfPay	
taxPaid    = grossPay * taxRate		
nettPay   = grossPay - taxPaid	

#Print emp statement
print("====== EMPLOYEE STATEMENT ======")
print(f"Employee name: {employeeName}")
print(f"Hours worked: {hoursWorked}")
print(f"Rate of pay: {rateOfPay}$")
print(f"Tax rate: {taxRate}")
print(f"Gross pay: {grossPay}$")
print(f"Tax paid: {taxPaid}$")
print(f"Nett pay: {nettPay}$")
print("================================")

