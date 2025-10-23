print("\nSTRING ANALYZER")
string_raw = input("Type anything here... :")
string = string_raw.lower()

vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")
numbers = list("0123456789")

vowel_count = 0
consonant_count = 0
number_count = 0
whitespace_count = 0
special_char_count = 0
for char in string:
  if char in vowels:
    vowel_count += 1
  elif char in consonants:
    consonant_count += 1
  elif char in numbers:
    number_count += 1
  elif char == " ":
    whitespace_count += 1
  else:
    special_char_count += 1

print(f"\n>>> {string_raw}")
print(f"{vowel_count} vowels, {consonant_count} consonants, {number_count} numbers, {whitespace_count} spaces, {special_char_count} special characters\n")
