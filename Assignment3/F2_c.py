# c) Read the contents of Myself.txt and reverse it and store it in the Myself.txt

with open("Myself.txt",'r') as f:
    content = f.read()

# Reverse the contents
rev = content[::-1]
# Write the reverse content to txt file
with open('Myself.txt','w')as f:
    f.write(rev)

print("Contents of Myself.txt have been reversed and updated")