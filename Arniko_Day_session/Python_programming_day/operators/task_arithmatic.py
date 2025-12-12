# write a program to calculate the actual bill to be paid by asking the user about the number of units bought and price per each unit after deducting discount amount and adding tax 
# ask the user about the number of units bought (int)
# ask the user about the price per unit  (float)
# declare variables for tax rate and discount rate
# calculate the total amount
# calculate the discount amount
# calculate the deducted amount 
# calculate the tax amount
# calculate the actual bill to be paid

# solution
no_of_units = int(input("Enter the number of units bought: "))
price_per_unit = float(input("Enter the price per unit: "))

discount_rate = 0.10
tax_rate = 0.08

total_amount = no_of_units * price_per_unit

discount_amt = total_amount * discount_rate

total_amount -= discount_amt # total_amount = total_amount - discount_amt

tax_amt = total_amount * tax_rate

total_amount += tax_amt # total_amount = total_amount + tax_amt

print(f"Actual amount to be paid: {total_amount}")
