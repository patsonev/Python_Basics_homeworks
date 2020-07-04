number_transactions = int(input())

balance = 0
counter=0

while counter < number_transactions:
    transaction = float(input())
    if transaction < 0:
        print('Invalid operation!')
        break
    balance += transaction
    print(f'Increase: {transaction:.2f}')
    counter += 1

print(f'Total: {balance:.2f}')