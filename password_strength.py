import math

print("\nPASSWORD STRENGTH METER\n")

print("--- Criteria ---")
print("1.) at least 8 characters")
print("2.) contains uppercase and lowercase")
print("3.) contains digits")
print("4.) contains special characters")
print("\nAdhering to these more will grant higher strength score.\n")

# validator
i = 0
while i <= 3:
  pwd = input("Test a password: ")
  if (pwd.isascii()) and (" " not in pwd) and (8 <= len(pwd) < 64):
    break
  i += 1
  if i == 3:
    print("Too many invalid attempts.\n") # only allows 3 attempts
    quit()
  elif not pwd.isascii(): # reject non-ascii chars
    print("Please use standard characters.\n")
  elif " " in pwd: # reject whitespaces
    print("Please use no spaces.\n")
  elif len(pwd) < 8:
    print("Please make a longer password.\n")
  elif len(pwd) >= 64:
    print("Please make a shorter password.\n")

# char categorizer
char_upper, char_lower, char_digits, char_special = [], [], [], [] # chars, listed per type
for char in pwd:
  if char.isupper(): # uppercase
    char_upper.append(char)
  elif char.islower(): # lowercase
    char_lower.append(char)
  elif char.isdecimal(): # digits
    char_digits.append(char)
  elif not char.isalnum(): # special characters
    char_special.append(char)

# single-char series detector
series_penalty = 0
for i in range(1, len(pwd)):
    if pwd[i] == pwd[i-1]:
        series_penalty += 1

# scoring
lu = len(char_upper)
ll = len(char_lower)
ld = len(char_digits)
ls = len(char_special)
xu = len(set(char_upper))
xl = len(set(char_lower))
xd = len(set(char_digits))
xs = len(set(char_special))
sp = series_penalty

diversity = (lu > 0) + (ll > 0) + (ld > 0) + (ls > 0)
distribution = (lu + ll + 2*ld + 3*ls) / len(pwd)
uniqueness = (xu + xl + xd + xs) / len(pwd) - math.log2(1 + sp / len(pwd))

score = 10*diversity + 8*distribution + 20*uniqueness + 5*math.log2(len(pwd))

# strength adjectives
print()
print(round(score, 2))
if score < 20:
  print("poor")
elif score < 50:
  print("weak")
elif score < 80:
  print("secure")
else:
  print("strong")
print()
