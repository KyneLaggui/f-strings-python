cash= int(input("Amount of Money you have?: "))
price_of_apple= int(input("How much does an apple cost?: "))

capacity_to_buy= cash//price_of_apple
change_to_an_apple= cash%price_of_apple

print(f"You can buy {capacity_to_buy} apples and your change is {change_to_an_apple} pesos.")