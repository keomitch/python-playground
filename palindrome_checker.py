print("\nPALINDROME CHECKER")

string_raw = input("Text goes here...: ")
string_processed = string_raw.lower().strip()
string_list_reversed = list(string_processed)[::-1]
string_reversed = "".join(string_list_reversed)
if string_processed == string_reversed:
  print("It's a palindrome!")
else:
  print("just a regular text :p")
print()
