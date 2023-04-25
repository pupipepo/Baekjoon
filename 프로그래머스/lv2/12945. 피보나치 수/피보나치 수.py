def fib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1
        
    for i in range(1,n):
        a,b = b, a+b

    return a
            
        
    
def solution(n):
    answer = fib(n)%1234567
    return answer
    

    