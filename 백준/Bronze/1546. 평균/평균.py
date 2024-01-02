n = int(input())
exam_scores=list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += 100*exam_scores[i]/max(exam_scores)
print(sum/n)