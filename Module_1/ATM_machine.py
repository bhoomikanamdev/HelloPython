# function_definition
def atm_machine(amount):
    count = 0
    currency_denomintion = [500, 200, 100, 50, 20, 10]
    for index in range(6):
        denom = currency_denomintion[index]
        count = count + int(amount / denom)
        amount = int(amount % denom)
    if amount > 0:
        count = -1
    return count


# function_execution
amt = int(input("Enter the amount- "))
count = atm_machine(amt)
print(count)

