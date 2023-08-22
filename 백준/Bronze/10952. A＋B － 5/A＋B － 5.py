A, B = input().split(' ')
ans_list=[]
while A!='0' or B!='0':
    ans_list.append(int(A)+int(B))
    A,B = input().split(' ')
for i in range(len(ans_list)):
    print(ans_list[i])