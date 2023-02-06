def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def print_20fact():
    for i in range(1,21):
        fact = factorial(i)
        print(str(i) + ".\t" + str(fact))
        

print_20fact()