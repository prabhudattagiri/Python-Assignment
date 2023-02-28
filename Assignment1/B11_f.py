# f) find and count number of words starts and ends with vowels in a string of multiple words
s=input("Enter a string of multiple words : ")
v=['a','e','i','o','u','A','E','I','O','U']
l=s.split(" ")
vword="" # word start and ends with vowels
count=0
for i in l:
    t=str(i)
    if (t[0] in v and t[-1] in v):
        vword+=t+" "
        count+=1

print("Total number of words that starts and ends with vowels is",count)
print("All word that start and end with vowel are :",vword)