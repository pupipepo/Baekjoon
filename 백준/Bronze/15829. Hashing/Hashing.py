import string
S = string.ascii_lowercase
index_reset_str='0'+S

num = int(input())
my_str = input()
hash = 0
for i in range(num):
    hash += index_reset_str.find(my_str[i])*(31**i)
hash = hash%1234567891
print(hash)