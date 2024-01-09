# a에 2를 곱한 수와 오른쪽에 1을 더한 수가 b보다 작으면 stack 에 계속 쌓자

a,b = map(int, input().split())
possible_nums=[(a,1)]
ans = -1
while possible_nums:
    this_num, count = possible_nums.pop()
    if this_num < b:
        possible_nums.append((this_num*2,count+1))
        possible_nums.append((this_num*10+1, count+1))
    elif this_num==b:
        ans = count
print(ans)