n = int(input())
d = list(range(n+1))
for i in range(2,int(n**0.5)+1):
    starting_point = i**2
    for j in range(starting_point, n+1):
        d[j] = min(d[j-starting_point]+1, d[j])
print(d[n])