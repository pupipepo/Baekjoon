trys = int(input())
for i in range(trys):
    h, w, n = map(int, input().split())
    y = n%h
    x = (n//h)+1
    if y==0:
        y=h
        x -=1
    if x<10:
        print(str(y)+'0'+str(x))
    else:
        print(str(y)+str(x))