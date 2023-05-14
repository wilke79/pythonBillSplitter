import random

lucky_one = ''
bill_partial = 0

number_friends = int(input('Enter the number of friends joining (including you):'))
if number_friends <= 0:
    print('\nNo one is joining for the party')
else:
    friends = {}
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(0, number_friends):
        friends[input()] = 0

    bill_value = int(input('\nEnter the total bill value:'))
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')

    if input() == 'Yes':
        lucky_one = random.choice(list(friends.keys()))
        print('\n%s is the lucky one!' %lucky_one)
        bill_partial = round(bill_value / (number_friends - 1), 2)
    else:
        print('No one is going to be lucky')
        bill_partial = round(bill_value / number_friends, 2)

    for friend in friends:
        if friend == lucky_one:
            pass
        else:
            friends[friend] = bill_partial
        
    print(f'\n{friends}')
