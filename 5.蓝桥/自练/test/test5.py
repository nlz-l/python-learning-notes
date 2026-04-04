import math
def sum_factorials(n:int)-> int:
    total = 0
    for i in range(1,n+1):
        total += math.factorial(i)
    return total
if __name__ == "__main__":
    print(sum_factorials(20))
    
