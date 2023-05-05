MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3


#Collecting user input (money deposit)
def deposit():
    while True:
        amount = input("What would you like to deposit (in 1000 IDR)? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
            
    return lines    
  
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between IDR {MIN_BET}000 - IDR {MAX_BET}000.")
        else:
            print("Please enter a number.")
            
    return amount  

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough money to bet that amount. Your current balance is IDR {balance}000.")
        else:
            break
    print(f"You are betting IDR {bet}000 on {lines} lines. Total bet is equal to IDR {total_bet}000")

main()
