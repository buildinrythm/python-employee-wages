# Welcome message
def welcomeMessage():
    print("Welcome to wage calculator")

# Calculate gross pay
def calculateGrossPay(hoursWorked, rateOfPay):
    return hoursWorked * rateOfPay

# Calculate tax paid
def calculateTaxPaid(grossPay, taxRate):
    return grossPay * taxRate

# Calculate Net
def calculateNett(grossPay, taxPaid, bonus):
    return grossPay - taxPaid + bonus


# Calculate bonus
def calculateBonus(hoursWorked):
        if hoursWorked >= 50:
            return  100
        elif hoursWorked >= 45:
            return  60
        elif hoursWorked >= 40:
            return  50
        else:
            return  0 

# Print emp statement
def printWages(employeeName, hoursWorked, rateOfPay, taxRate, grossPay, taxPaid, nettPay, bonus):
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

# Closing message
def closingMessage():
    print("Thankyou for using wage calculator goodbye!")

#Main program

#Variables
employeeName = ""
hoursWorked = 0
rateOfPay = 0.00
taxRate = 0.00
bonus = 0
completed = True

while completed:
    # Get user input
    employeeName = input("Enter you name")
    hoursWorked = float(input("Enter hours worked"))
    rateOfPay = float(input("Enter rate of pay"))
    taxRate = float(input("enter tax rate")) / 100

    grossPay = calculateGrossPay(hoursWorked, rateOfPay)
    taxPaid = calculateTaxPaid(grossPay, taxRate)
    bonus = calculateBonus(hoursWorked)
    nettPay = calculateNett(grossPay, taxPaid, bonus)

# Print results
    printWages(
        employeeName,
        hoursWorked,
        rateOfPay,
        taxRate,
        grossPay,
        taxPaid,
        nettPay,
        bonus
    )

    completed = input("Add another user (y/n): ").strip().lower() == "y"

closingMessage()