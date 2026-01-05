#Variables
employeeName = ""
hoursWorked = 0
rateOfPay = 0.00
taxRate = 0.00
bonus = 0

# Get user input
employeeName = input("Enter you name")
hoursWorked = int(input("Enter hours worked"))
rateOfPay = float(input("Enter rate of pay"))
taxRate = float(input("enter tax rate")) / 100


# Calculations
grossPay = hoursWorked * rateOfPay	
taxPaid    = grossPay * taxRate		
nettPay   = grossPay - taxPaid	

if hoursWorked >= 50:
    bonus = 100
elif hoursWorked >= 45:
    bonus = 60
elif hoursWorked >= 40:
    bonus = 50
else:
    bonus = 0

nettPay += bonus

#Print emp statement
print("====== EMPLOYEE STATEMENT ======")
print(f"Employee name:\t {employeeName}")
print(f"Hours worked:\t {hoursWorked}")
print(f"Rate of pay:\t ${rateOfPay}")
print(f"Tax rate:\t {taxRate:.2f}%")
print(f"Gross pay:\t ${grossPay:.2f}")
print(f"Tax paid:\t ${taxPaid:.2f}")
print(f"Nett pay:\t ${nettPay:.2f}")
print(f"Bonus:\t\t ${bonus}")
print("================================")

