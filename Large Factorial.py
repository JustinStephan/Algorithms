def factorial(n):
    calculated = [1]
    if n == 1 or n == 0:
        return 1
    
    else:
        for i in range(1,n):
            #print(i)
             calculated.append(i * calculated[i-1])
        return n *calculated[n-1]

def numCount(num):
    count=0
    while num > 0:
        num //= 10
        count +=1
    return count

while True:
    n = int(input('How many decimel places of Pi would you like to calculate?'))
    # sqr(8)/9801
    #termA = (babylon(8,5,1))/9801
    #print(termA)
    # 4n!
    fact = factorial(n)
    print(fact)
    print(numCount(fact))
    
