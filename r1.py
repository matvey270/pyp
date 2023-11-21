with open('17.txt') as j:
    a=[int(i) for i in j]
cnt=0
n=len(a)
min_s=-10**10
for i in range(n-2):
    x,y,z=a[i],a[i+1],a[i+2]
    print(x,y,z)
    if x**2==y**2+z**2 or y**2==x**2+z**2 or z**2==y**2+x**2 :
        cnt+=1
        min_s=min(x+y+z, min_s)
        
print(cnt,min_s)