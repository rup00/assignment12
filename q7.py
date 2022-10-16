
def co_prime(a, b): 
  
    if (b == 0): 
        return a 
    return co_prime(b, a % b) 
  

def check_coprime(a, b): 
  
    if (co_prime(a, b) == 1): 
        print("Co-Prime") 
    else: 
        print("Not Co-Prime") 
  

a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
check_coprime(a, b) 
