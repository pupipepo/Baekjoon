import string
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
counts = [0]*26
my_str = input().lower()
for str in my_str:
    for i in range(26):
        if str == alphabet_lower[i]:
            counts[i] += 1
max1 = max(counts)
max1_index = counts.index(max1)
counts.pop(max1_index)
max2 = max(counts)
if max1 == max2:
    print('?')
else:
    print(alphabet_upper[max1_index])