K = int(input())
arr = []
for i in range(0,K) :
    val = int(input())
    if val == 0 :
        arr.pop()
    else :
        arr.append(val)
print(sum(arr))