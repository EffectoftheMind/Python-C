item_name = input('Enter food item name:\n')
item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n'))

# FIXME (1): Finish reading item price and quantity, then output a receipt
item_cost = item_price * item_quantity
total_cost = item_price * item_quantity
print()
print('RECEIPT')
print(item_quantity, item_name, "@", f'${item_price:.2f}', "=", f'${item_cost:.2f}')
print("Total cost:", f'${total_cost:.2f}')
print()
print()
   
# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt

second_name = input('Enter second food item name:\n')
second_price = float(input('Enter item price:\n'))
second_quantity = int(input('Enter item quantity:\n'))

total_cost = (item_price * item_quantity) + (second_price * second_quantity)
item2_cost = second_price * second_quantity

print()
print('RECEIPT')
print(item_quantity, item_name, "@", f'${item_price:.2f}', "=", f'${item_cost:.2f}')
print(second_quantity, second_name, "@", f'${second_price:.2f}', "=", f'${item2_cost:.2f}')
print("Total cost:", f'${total_cost:.2f}')
print()

# FIXME (3): Add a gratuity and total with tip to the second receipt

gratuity = .15 * total_cost
end_total = gratuity + total_cost
print("15% gratuity:", f'${gratuity:.2f}')
print("Total with tip:", f'${end_total:.2f}')
