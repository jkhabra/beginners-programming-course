def nestEggFixed(salary, save, growthRate, years):
    """
    Return a integer list whose values are the size of retirement account at
      the end of each year
    """
    total_balance = []
    first_year = salary * save * 0.01
    growth = 1 + 0.01 * growthRate

    for i in range(years):
        if i == 0:
            total_balance.append(first_year)
        else:
            total_balance.append(total_balance[-1] * growth + first_year)

    return total_balance


def nestEggVariable(salary, save, growthRates):
    """
    Return a list of retirement account value at the end of each year
    """
    total_balance = []
    first_year = salary * save * 0.01

    for i in range(len(growthRates)):

        if i == 0:
            total_balance.append(first_year)
        else:
            total_balance.append((total_balance[-1]) *
                                 (1 + 0.01 * growthRates[i])
                                 + (first_year))

    return total_balance


def postRetirement(savings, growthRates, expenses):
    """
    Return a list of retirement account value at the end of each year
    """
    total_balance = []

    for i in range(len(growthRates)):
        if i == 0:
            total_balance.append((savings) *
                                 (1 + 0.01 * growthRates[i]) -
                                 expenses)
        else:
            total_balance.append((total_balance[-1]) *
                                 (1 + 0.01 * growthRates[i]) -
                                 (expenses))
        print(total_balance)

    return total_balance
