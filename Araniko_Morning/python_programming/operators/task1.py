# Write a program to calculate the total bill to be paid of several units of items after deducting discount and adding tax 
# ask the user to input number of units (int)
# ask the user to input price per unit (float)
# declare the variables for discount_rate(10%) and tax_rate(8%)
# calulate total amount
# calculate the discount amount
# calculate tax amount from deducted total amount from discount
# calculate actual amount

discount_rate = 0.10
tax_rate = 0.08

unit = int(input("Enter the number of units bought: "))
price_per_unit = float(input("Enter the price per unit: "))

total_amount = unit * price_per_unit

discount_amount = discount_rate * total_amount

amount_after_discount = total_amount - discount_amount

tax_amount = tax_rate * amount_after_discount

actual_amount = amount_after_discount + tax_amount

print(f"Actual amount to be paid by buyer is {actual_amount}")

