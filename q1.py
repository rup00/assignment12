
number = int(input("Enter a number: "))

reverse = 0

while(number > 0):
    reminder = number % 10
    reverse = (reverse * 10) + reminder
    number = number // 10

print("Reverse of entered number is = %d" % reverse)