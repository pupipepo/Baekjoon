n = int(input())
num_list = sorted(list(map(int, input().split())))
if n%2==1:
    print(num_list[n//2]**2)
else:
    print(min(num_list)*max(num_list))