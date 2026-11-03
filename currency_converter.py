import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

money_art = """
||/=========================================================================/||
||  (100)=============| Abdelmotagaly currency converter |=============(100)  ||
||  << /        /$\                                              /$\ >> ||
||  << /       / || \                                           / || \ >> ||
||  <<       12  ||| \             L38036133B        L38036133B  12  >> ||
||  <<           |||               $$ --- /                      >> ||
||  <<            \$               $$ --- /         One Hundred       >> ||
||||/$\===========================|  _ _ _  |===========================/$\||||
||  (100)=============| Abdelmotagaly currency converter |=============(100)  ||
||  \\$/         /$\               _______                       \\$/  ||
||   >>   12    / || \            /   _   \          L38036133B   >>    ||
||   >>        /  ||| \          ||  (_)  ||                       >>   ||
||   >>       L38036133B          |   _   |         One Hundred    >>   ||
||   >>   12      |||       12    \_______/   Series     12        >>   ||
||  //$\       Treasurer          /Franklin\   1989               //$\  ||
||  ||/======================-|UNITED STATES OF AMERICA|-===================/||  
||  (100)===================== ONE HUNDRED DOLLARS =====================(100)  ||
||\\=========================================================================\\||
"""

currencies = {
    "USD": 1.0,
    "EUR": 0.85,
    "EGP": 30.9,
    "RMB": 6.5
}

while True:
    clear_screen()
    print("Welcome to 'currency converter':")
    print(money_art)
    print("""---------------------------------------------------------------------------------
USD : 1.0
EUR : 0.85
EGP : 30.9
RMB : 6.5
---------------------------------------------------------------------------------""")
    
    convert_from_currency = input("Choose a currency to convert from: ").upper()
    if convert_from_currency in currencies:
        convert_from_currency_value = currencies[convert_from_currency]
    else:
        print("Invalid currency. Please choose one of the listed currencies!")
        time.sleep(2)
        continue
        
    while True:
        try:
            convert_amount = int(input("Enter the amount: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        confirm_amount = input(f"You entered {convert_amount}. Confirm (y/n): ").lower()
        if confirm_amount == "n":
            continue
        else:
            break
            
    clear_screen()
    
    convert_to_currency = input("Choose a currency to convert to: ").upper()
    if convert_to_currency in currencies:
        convert_to_currency_value = currencies[convert_to_currency]
    else:
        print("Invalid currency. Transaction cancelled.")
        time.sleep(2)
        continue
        
    exchange_rate = convert_to_currency_value / convert_from_currency_value
    converted_money = exchange_rate * convert_amount
    
    time.sleep(1)
    print("Analyzing your request... please wait.")
    time.sleep(2)
    print(f"Checking for {convert_to_currency}'s best rates available...please wait.")
    time.sleep(1)
    print(f"Getting a discount price for {convert_from_currency}...please wait.")
    
    clear_screen()
    time.sleep(0.5)
    print(f"Preparing the deal from {convert_from_currency} to {convert_to_currency}...please wait.")
    time.sleep(1.5)
    
    print(f"Exchange rate: 1 {convert_from_currency} = {exchange_rate:.4f} {convert_to_currency}")
    print(f"{convert_amount} {convert_from_currency} is equal to {converted_money:.2f} {convert_to_currency}")
    time.sleep(1)
    
    confirm_conversion = input("Do you accept this transaction (y/n): ").lower()
    if confirm_conversion == "y":
        print("\nTransaction completed! (: ")
    else:
        print("\nTransaction cancelled. ): ")
        
    print("----------------")
    another_conversion = input("Do you want to perform another conversion (y/n): ").lower()
    if another_conversion != "y":
        print("Thank you for using Abdelmotagaly currency converter! Goodbye.")
        break
