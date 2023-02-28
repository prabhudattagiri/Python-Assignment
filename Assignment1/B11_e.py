# e) create a list to store unique character in string and another list to store frequency of repeatation 
# of unique character available in first list in the string
s = input("Enter a String : ")
unique = list(set(s)) # Convert to set (set contain only unique item)
frequency = []

for char in unique:
    count = s.count(char)
    frequency.append(count)

print("Unique characters:", unique)
print("Frequency of repetition:", frequency)
