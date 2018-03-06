import time
n = 100
notprime = [1]*(n+1)
prime =[0]*(n+1)
count = 0

start =time.time()
for i in range(2,n):
    if notprime[i]==1:
        prime[count]=i
        count+=1
    
    for j in range(0,count):
        if i*prime[j]<=n:
            notprime[i*prime[j]]=0
            if i%prime[j]==0:
                break
            
end = time.time()
print(end-start)
print(prime)