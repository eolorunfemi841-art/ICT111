item_name = input("Enter item name: ").strip().title()
unit_price = float(input("Enter price: ")) 
quantity = int(input("Quantity"))
total = unit_price * quantity
print(f"Items:{item_name} : Price k{total: .2f}")