n, m = map(int, input().split(' '))
strings = []
for i in range(n):
    strings.append(input())
B_start_counts=[] #짝수 번째 row 에서는 짝수가 B / 홀수번째 row에서는 홀수가 B
W_start_counts=[]
n_rows = n-8+1
n_cols = m-8+1
for i in range(n_rows):
    for j in range(n_cols):
        ans_B = 0
        ans_W = 0
        for num_rows in range(8):
            for num_cols in range(8):
                test_string = strings[i+num_rows][j+num_cols]
                if num_rows%2==0:
                    if num_cols%2==0:
                        ans_B += test_string != 'B'
                        ans_W += test_string != 'W'
                    else:
                        ans_B += test_string != 'W'
                        ans_W += test_string != 'B'
                else:
                    if num_cols%2==0:
                        ans_B += test_string != 'W'
                        ans_W += test_string != 'B'
                    else:
                        ans_B += test_string != 'B'
                        ans_W += test_string != 'W'
        B_start_counts.append(ans_B)
        W_start_counts.append(ans_W)
min_B = min(B_start_counts)
min_W = min(W_start_counts)
print(min(min_W, min_B))