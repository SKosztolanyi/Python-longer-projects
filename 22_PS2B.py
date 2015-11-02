Minimum_monthly_payment = 10
balance = 6891
annualInterestRate = 0.18
b=balance
Monthly_interest_rate= annualInterestRate/12.0

while True:
    Minimum_monthly_payment+=10
    balance = b
    for i in range(12):
        remaining_balance = balance - Minimum_monthly_payment
        balance = remaining_balance + Monthly_interest_rate * remaining_balance
    if balance <= 0:
        print "Lowest payment: " + str(Minimum_monthly_payment)
        break