
def next_prime(num):
    while True:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            return num
etr=int(input("enter the number to print its next prime:"))
print(next_prime(etr))