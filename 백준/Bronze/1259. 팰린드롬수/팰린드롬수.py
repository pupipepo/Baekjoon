while True:
    num=input()
    if num=='0':
        break
    else:
        back_num=num[::-1]
        flag=0
        for i in range(len(num)//2):
            if num[i]!=back_num[i]:
                flag+=1
        if flag==0:
            print('yes')
        else:
            print('no')