print("\nNUMBER CLASSIFIER")

# input validator
while True:
  try:
    number_input = input("Please give a number: ")
    if number_input == "q": # choice to quit
      print()
      quit()
    if "." in number_input: # float input
      number = float(number_input)
    else: # integer input
      number = int(number_input)
    break
  except ValueError:
    print("Enter a number, please...\n[or type 'q' to quit]\n")

# positive/negative selector
if number < 0:
   print(f"{number} is a negative number.")
elif number == 0:
   print(f"{number} is a neutral number (zero).")
elif number > 0:
   print(f"{number} is a positive number.")

# even/odd selector
if number % 2 == 0:
   print(f"{number} is an even number.")
elif number % 2 == 1:
   print(f"{number} is an odd number.")
else: # non-integer values
   print(f"{number} is not an even nor an odd number.")

# digit counter
number_listed = list(number_input)
if "." in number_input: # check if the number is a float
  number_listed.remove(".")
if "-" in number_input: # check if the number is negative
  number_listed.remove("-")
if len(number_listed) == 1:
  print(f"{number} is a single-digit number.")
else:
  print(f"{number} is {len(number_listed)} digits long.")

print()
