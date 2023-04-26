nums = list(range(1,10001))
ans=[]
for i in range(1, 10000):
    if i in nums:
        ans.append(i)
        nums.remove(i)
        if ((i)+i//1000+(i%1000)//100+(i%100)//10+i%10) in nums:
            nums.remove((i)+i//1000+(i%1000)//100+(i%100)//10+i%10)
    else:
        if ((i)+i//1000+(i%1000)//100+(i%100)//10+i%10) in nums:
            nums.remove((i)+i//1000+(i%1000)//100+(i%100)//10+i%10)
for j in ans:
    print(j)