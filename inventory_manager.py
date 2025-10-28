inventory = {
  "Keyboard": {"stock": 15, "price" : 45.00},
  "Monitor": {"stock": 5, "price" : 199.99}
}

def add_item(inventory_dict):
  item_name = input("Enter item name: ").capitalize()

  # Check if the item already exists using 'in'
  if item_name in inventory_dict:
    print(f"'{item_name}' already exists. Use Option 2 to update it.")
    return

  # Get Stock
  try:
    stock = int(input("Enter initial stock quantity: "))
    price = float(input("Enter unit price: $"))
  except ValueError:
    print("Invalid input for stock or price. Must be a number.")
    return

  # Add the new entry to the inventory dictionary
  inventory_dict[item_name] = {"stock": stock, "price": price}
  print(f"Item '{item_name}' added.")

def update_item(inventory_dict):
  item_name = input("Enter the name of the item to update: ").capitalize()

  # Check if the item is in the dictionary
  if item_name not in inventory_dict:
    print(f"Error: Item '{item_name}' not found in inventory.")
    return

  print(f"\nCurrently updating: {item_name} (Stock: {inventory_dict[item_name]['stock']}, Price: ${inventory_dict[item_name]['price']:.2f})")

  # Get update choice
  update_choice = input("Update (S)tock or (P)rice? ").upper()

  try:
    if update_choice == 'S':
      new_stock = int(input("Enter new stock quantity: "))
      inventory_dict[item_name]['stock'] = new_stock
      print(f"Stock for '{item_name}' updated to {new_stock}.")
    elif update_choice == 'P':
      new_price = float(input("Enter new unit price: $"))
      inventory_dict[item_name]['price'] = new_price
      print(f"Price for '{item_name}' updated to ${new_price:.2f}.")
    else:
      print("Invalid update choice.")
  except ValueError:
    print("Invalid input. Please ensure stock is an integer and price is a number.")

def view_inventory(inventory_dict):
  if not inventory_dict:
    print("Inventory is currently empty.")
    return

  print("\n--- Current Inventory ---")
  print(f"{'ITEM':<15}{'STOCK':<10}{'PRICE':<10}")
  print("-" * 35)

  # Loop through the inventory items. The .items() method returns (key, value) pairs.
  for item, details in inventory_dict.items():
    stock = details['stock']
    price = details['price']

    # Print using f-strings for formatted output
    print(f"{item:<15}{stock:<10}${price:,.2f}")

def main():
  halt = False
  while halt == False:
    print("\n--- Inventory Management System ---")
    print("1. Add New Item")
    print("2. Update Stock/Price")
    print("3. View Inventory")
    print("4. Exit")
    choice = input("Enter your choice [1-4]: ")

    if choice == '1':
      add_item(inventory)
    elif choice == '2':
      update_item(inventory)
    elif choice == '3':
      view_inventory(inventory)
    elif choice == '4':
      print("Exiting program...\n")
      halt = True
    else:
      print("Please input a valid choice.")

if __name__ == "__main__":
  main()
