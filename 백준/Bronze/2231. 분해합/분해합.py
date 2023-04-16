num = int(input())
ans_list=[]
for i in range(num):
    str_length = len(str(i)) # 몇자리 수인지 확인
    test=i # 자기 자신을 더하기
    for j in range(str_length):
        test += int(str(i)[j])
    if test==num:
        ans_list.append(i)
try:
    print(ans_list[0])
except:
    print(0)