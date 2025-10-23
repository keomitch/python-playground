print("\nWORD COUNTER")

sentence = input("Type a sentence here...: ")
print(f"\n>>> {sentence}")

word_list = sentence.lower().split(" ")
frequent_word = ""
frequent_word_count = 0
frequent_word_count_list = []

print("--- Word Count ---")
for word in sorted(set(word_list)):
  word_count = word_list.count(word)
  if word_count >= frequent_word_count:
    frequent_word = word
    frequent_word_count = word_count
    frequent_word_count_list.append(frequent_word_count)
  print(f"{word}: {word_count}")

if frequent_word_count_list.count(frequent_word_count) == 1:
  print(f"\nThe most frequent word: {frequent_word} ({frequent_word_count} times)")

print()
