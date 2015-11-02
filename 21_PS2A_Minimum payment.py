Month = 0
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total=0

for i in range(12):
    Monthly_interest_rate= (annualInterestRate) / 12.0
    Minimum_monthly_payment = (monthlyPaymentRate) * (balance)
    Monthly_unpaid_balance = (balance) - (Minimum_monthly_payment)
    Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
    round(Updated_balance_each_month, 2)
    Month+=1
    balance=Updated_balance_each_month
    total+=Minimum_monthly_payment
    print "Month: "+ str(Month)
    print "Minimum monthly payment: " + str(round(Minimum_monthly_payment, 2))
    print "Remaining balance: " + str (round(balance, 2))

print "Total paid: " + str(round(total, 2))
print "Remaining balance: " + str (round(balance, 2))