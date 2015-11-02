balance = 6891
annualInterestRate = 0.18
b=balance
Monthly_interest_rate= annualInterestRate/12.0
MP_lower_bound = balance/12
MP_upper_bound = (balance*(1+Monthly_interest_rate)**12)/12.0
Minimum_monthly_payment = (MP_lower_bound+MP_upper_bound)/2

while True:
    Minimum_monthly_payment = (MP_lower_bound+MP_upper_bound)/2
    balance = b
    for i in range(12):
        remaining_balance = balance - Minimum_monthly_payment
        balance = remaining_balance + Monthly_interest_rate * remaining_balance
    if (abs(balance-0)) < 0.1:
        print "Lowest payment: " + str(round(Minimum_monthly_payment, 2))
        break
    else:
        if balance >0:
            MP_lower_bound=Minimum_monthly_payment
        elif balance <0:
            MP_upper_bound=Minimum_monthly_payment