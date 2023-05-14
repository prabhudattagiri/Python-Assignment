# 10. Wap to generate prime numbers in between 10 to 50 and store it in list ,find avg of all prime number in the list ,check for 
# palindrome numbers available in the list and store in another list,Display no of elements with elements in prime list and also 
# display no of elements with elements in palindrome list using multiple inheritance

class Prime:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.primeList = []  # Empty list

    def isPrime(self, n):
        if n <= 1:
            return False
        
        for i in range(2, (n //2) + 1):
            if n % i == 0:
                return False
        return True

    def getPrimeNum(self):
        for i in range(self.start, self.end + 1):
            if self.isPrime(i):
                self.primeList.append(i)

class Palindrome:
    def __init__(self, l):
        self.li = l
        self.palindromeList = []
    
    def checkPalindrome(self):
        for i in self.li:
            if str(i) == str(i)[::-1]:  # if num == reversenum
                self.palindromeList.append(i)

class Number(Prime, Palindrome):
    def __init__(self, start, end):
        Prime.__init__(self, start, end)
        Prime.getPrimeNum(self)  # Call getPrimeNum from Prime class
        Palindrome.__init__(self, self.primeList)

    def calculateAverage(self):
        sumOfPrime = sum(self.primeList)  # sum of all prime num
        totalPrime = len(self.primeList)  # total no of prime num
        return (sumOfPrime / totalPrime)

    def display_counts(self):
        prime_count = len(self.primeList)
        palindrome_count = len(self.palindromeList)
        print("Number of elements in prime list:", prime_count)
        print("Number of elements in palindrome list:", palindrome_count)

# In main
obj = Number(10, 50)  # start=10 end=50
# Calculate the average of prime number
avg = obj.calculateAverage()
print("Average of prime numbers is", avg)
# Check palindrome number
obj.checkPalindrome()
# Display counts of both (prime & palindrome)
obj.display_counts()