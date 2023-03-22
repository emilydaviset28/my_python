number = int(input("Enter a number: "))
reverse_number = 0
while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number //= 10
print("Reverse number:", reverse_number)
