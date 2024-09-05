# Ariana Fayehun
# Date: 9/4/24
# This is the solution for the second coding challenge


# Constant variables for Pennsylvania tax and the price for each meal
PA_TAX = 0.06
PRICE_OF_MEAL = 12.49


# These variables calculate the results for the tax per meal, total without tax, and the total with tax
tax_per_meal = PRICE_OF_MEAL *  PA_TAX
total_without_tax = PRICE_OF_MEAL * 5
total_with_tax = (tax_per_meal * 5) + total_without_tax


#This prints the results of the calculations
print()
print("| Lunch Spending Habits |")
print("-------------------------")
print(f"Tax per meal: {tax_per_meal}")
print(f"Total without tax: {total_without_tax}")
print(f"Total with tax: {total_with_tax}")
print("-------------------------")
print()