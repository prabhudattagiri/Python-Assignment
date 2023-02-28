# d) Find the letter used maximum and minimum time in a string
s=input("Enter a string : ")
letter_count = {}

# count the occurrence of each letter in the string
for letter in s:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

# find the letter used maximum and minimum times
max_count = 0
min_count = len(s)
max_letter = ""
min_letter = ""

for letter, count in letter_count.items():
    if count > max_count:
        max_count = count
        max_letter = letter
    if count < min_count:
        min_count = count
        min_letter = letter

print("Letter used maximum times is:", max_letter)
print("Letter used minimum times is:", min_letter)
