import pandas as pd 
groceries = pd.read_csv('early_november_groceries.csv')

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

owes_owed = lambda num: 'owes' if num >= 0 else 'is owed'

print('Wesley {} {} GBP this month'.format(owes_owed(wes_owes),round(abs(wes_owes),2)))
print('Jack {} {} GBP this month'.format(owes_owed(jack_owes),round(abs(jack_owes),2)))
print('Eddie {} {} GBP this month'.format(owes_owed(eddie_owes),round(abs(eddie_owes),2)))







