m = int(input())
list = []
for i in range(m,-1,-1):
    list.append(i)
for i in range(1,m+1):
    list.append(i)
print(" ".join(str(item) for item in list))