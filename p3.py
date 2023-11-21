with open('17-3.txt') as l:
    a=[int(i) for i in l]
n=len(a)
cnt=0
mx=-10**9

for i in range(n-1):
    x,y=a[i],a[i+1]
    if x%2==0 and x%4==0 and y%2!=0 and y%11==0 or y%2==0 and y%4==0 and x%2!=0 and x%11==0:
        cnt+=1
        mx=max(mx, x+y)
print(cnt, mx)
