# Start here
import pandas as pd 
groceries = pd.read_csv('october_groceries.csv')

total = groceries.cost.sum() *-1
transactions_w = groceries[groceries.person == 'Wesley']
wes_spent = transactions_w.cost.sum() *-1
transactions_e = groceries[groceries.person == 'Eddie']
eddie_spent = transactions_e.cost.sum() *-1
transactions_j = groceries[groceries.person == 'Jack']
jack_spent = transactions_j.cost.sum() *-1
share = total / 3

wes_owes = share - wes_spent
eddie_owes = share - eddie_spent
jack_owes = share - jack_spent

print('Wesley owes {} GBP this month'.format(round(wes_owes,2)))
print('Jack owes {} GBP this month'.format(round(jack_owes,2)))
print('Eddie owes {} GBP this month'.format(round(eddie_owes,2)))







