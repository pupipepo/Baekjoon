n_try = int(input())
ans=[]
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if (i != j) & (j != k) & (k != i):
                ans.append(f'{i}{j}{k}')
for i in range(n_try):
    new_ans=[]
    num, strike, ball = map(int, input().split(' '))
    num = str(num)
    for num_string in ans:
        strike_count, ball_count = 0, 0
        if num_string[0] == num[0]:
            strike_count+=1
        if num_string[1] == num[1]:
            strike_count+=1
        if num_string[2] == num[2]:
            strike_count+=1
        if num_string[0] == num[1] or num_string[0] == num[2]:
            ball_count+=1
        if num_string[1] == num[0] or num_string[1] == num[2]:
            ball_count+=1
        if num_string[2] == num[0] or num_string[2] == num[1]:
            ball_count+=1
        if strike_count == strike and ball_count==ball:
            new_ans.append(num_string)
    ans = new_ans
print(len(ans))