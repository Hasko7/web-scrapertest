## Slot machine
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
def deposit():
    while True:
        amount = input("Please give your deposit in $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must greater than zero")
        else:
            print("Amount must be a number")
    return amount

def get_number_lines():
    while True:
        lines = input("Give the number of lines (1 -" + str(MAX_LINES) + ")")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines (1-3)")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} to ${MAX_BET}")
        else:
            print("Bet must be a number")
    return amount


def main():
    balance = deposit()
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, you current balance is ${balance}")
        else:
            break

    print(f"Youre betting ${bet} on {lines} Lines. Youre total bet is ${total_bet}.")


main()



