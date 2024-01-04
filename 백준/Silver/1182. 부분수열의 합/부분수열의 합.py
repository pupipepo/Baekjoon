from itertools import combinations

n, s = map(int, input().split(' '))
ans=0
num_list = list(map(int, input().split(' ')))
for i in range(1,n+1):
    part_list = list(combinations(num_list, i))
    for j in range(len(part_list)):
        if sum(part_list[j])==s:
            ans+=1
print(ans)