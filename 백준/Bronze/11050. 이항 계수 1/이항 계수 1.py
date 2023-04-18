n, k = map(int, input().split())
if n == k or k==0:
    print(1)
else:
    ans=1
    for i in range(k):
        ans *= n
        ans /= k
        n -= 1
        k -= 1
    print(round(ans))