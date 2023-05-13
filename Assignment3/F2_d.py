# d) Read the contents of Myself.txt and compare it with the content of backup.txt to findout palindrome strings

# Read the contents of Myself.txt
with open("Myself.txt", "r") as myself_file:
    myself_content = myself_file.read().replace('\n', '')

# Read the contents of backup.txt
with open("backup.txt", "r") as backup_file:
    backup_content = backup_file.read().replace('\n', '')

# Function to check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

# Find palindrome strings in the contents
myself_palindromes = [word for word in myself_content.split() if is_palindrome(word)]
backup_palindromes = [word for word in backup_content.split() if is_palindrome(word)]

# Print the palindromes found in Myself.txt
print("Palindrome strings in Myself.txt:")
for word in myself_palindromes:
    print(word)

# Print the palindromes found in backup.txt
print("Palindrome strings in backup.txt:")
for word in backup_palindromes:
    print(word)