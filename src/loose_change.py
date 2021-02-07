def loose_change(cents):
    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    coins = {5:'Nickels',1: 'Pennies',10: 'Dimes',25: 'Quarters'}
    rest = int(cents)
    for val,name in sorted(coins.items(),key=lambda x:-x[0]):
        if rest < val:
            continue
        n_coins = rest//val
        change_dict[name] = n_coins
        rest -= n_coins*val
        if rest == 0:
            break
    print(change_dict)
    return change_dict

print(loose_change(29))