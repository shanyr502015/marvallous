num = int(input("Enter a number: "))

reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")