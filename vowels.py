def contains_all_vowels(sentence):
# Define a set of all vowels
vowels = set("AEIOU")
# Convert the input sentence to uppercase to handle both uppercase and lowercase
letters
sentence = sentence.upper()
# Check if all vowels are present in the sentence
for vowel in vowels:
if vowel not in sentence:
return False
return True
# Test the function with the provided words
words = ["EDUCATION", "AUTOMOBILE", "EVACUATION", "REMUNERATION", "REGULATION"]
for word in words:
if contains_all_vowels(word):
print(f"{word} contains all vowels.")
else:
print(f"{word} does not contain all vowels.")
