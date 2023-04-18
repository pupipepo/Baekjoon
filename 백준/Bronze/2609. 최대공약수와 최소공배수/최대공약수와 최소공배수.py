def gcd(n, m):
    while n != 0:
        t = m%n
        (m,n) = (n,t)
    return abs(m)
    
a, b = map(int, input().split())
g = gcd(a, b)
l = (a//g)*(b//g)*g

print(g)
print(l)