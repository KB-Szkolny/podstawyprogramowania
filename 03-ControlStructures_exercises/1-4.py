###
# Credit card payment 
#
account_balance = 500
total_payment = float(input('Wpisz kwote transakcji: '))

if total_payment < account_balance:
    print('Payment completed')
else:
    print('No funds')