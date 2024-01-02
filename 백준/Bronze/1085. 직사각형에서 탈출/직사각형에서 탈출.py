x,y,w,h=map(int, input().split(' '))
to_end=[x,y,w-x,h-y]
print(min(to_end))