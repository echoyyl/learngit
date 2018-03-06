n = 100
num = [1]*n

for i in range(2,n):
    if  i*i<n and num[i]==1:
        for j in range(2*i,n,i):
            num[j]=0
            
for i in range(2,len(num)):
    if num[i]==1:
        print(i)