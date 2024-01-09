case_ind = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 & p==0 & v==0:
        break
    else:
        ans = (v//p)*l + min(v%p, l)
        print(f'Case {case_ind}: {ans}')
        case_ind += 1