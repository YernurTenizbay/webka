n=int(input())
a=[]
cnt=0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(a[i]>0):
        cnt+=1
print(cnt)