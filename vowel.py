text = input("Enter a string: ")

print("You entered:", text) #print entered string 

vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1   # Count vowels

print("Number of vowels:", count)