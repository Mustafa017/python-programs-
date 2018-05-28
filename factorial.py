def rec_fact(x):
    if x == 1:
        return 1
    else:
        return (x*rec_fact(x-1))
print(rec_fact(4))

#Andela challenge
def factorial(n):
    if n<1:
        return "Number should be greater or equal to 1"
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
        
print(factorial(8))