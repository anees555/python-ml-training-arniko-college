discount_rate = 0.10
tax_rate = 0.08

unit = int(input("Enter the number of units bought: "))
price_per_unit = float(input("Enter the price per unit: "))

total_amount = unit * price_per_unit


discount_amount = discount_rate * total_amount

total_amount -= discount_amount

tax_amount = tax_rate * total_amount

total_amount +=  tax_amount

print(f"Actual amount to be paid by buyer is {total_amount}")