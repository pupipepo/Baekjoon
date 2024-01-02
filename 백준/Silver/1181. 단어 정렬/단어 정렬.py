n = int(input())
word_list=[]
for i in range(n):
    word=input()
    if word in word_list:
        pass
    else:
        word_list.append(word)
word_list.sort()
length_list=[]
for j in range(len(word_list)):
    length_list.append(len(word_list[j]))
arranged_list=[]
for i in range(max(length_list)+1):
    while i in length_list:
        arranged_list.append(word_list[length_list.index(i)])
        word_list.pop(length_list.index(i))
        length_list.pop(length_list.index(i))
for k in range(len(arranged_list)):
    print(arranged_list[k])