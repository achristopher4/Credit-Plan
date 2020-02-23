
initial = float(input("Enter the puchase price: "))

downPayment = 0.1
annualInterestRate = 0.12
monthlyPayment = 0.05
fixed = initial * monthlyPayment

month = 0
amount = 1
endBalance = 1
principal = 0

payment = initial * downPayment
payment = initial - payment
fixed = payment * monthlyPayment

print("%0s%20s%10s%15s%15s%20s" % ("Month", "Starting Balance", "Interest", "Principal", "Payment", "Ending Balance"))

while amount > principal:
    month += 1

    amount = payment

    if amount - principal > 0:
        interest = payment * (annualInterestRate / 12)
    else:
        interest = 0

    if amount - principal > 0:
        principal = fixed - interest
    else:
        principal = amount

    if amount - principal > 0:
        amountDue = fixed
    else:
        amountDue = amount

    payment = amount - principal

    if amount - principal > 0:
        endBalance = payment
    else:
        endBalance = 0
    
    print("%3d Month%10.2f%15.2f%13.2f%16.2f%16.2f" %(month, amount, interest, principal, amountDue,endBalance))
