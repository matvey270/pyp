with open('17-9.txt') as l:            ###195
    a=[int(i) for i in l]
n=len(a)
cnt=0
mx=[]

def f(x):
    x=bin(x)
    po=0
    pl=0
    for i in x:
        if i == '0':
            po+=1
        else:
            pl+=1
    if po>=1 and pl>=3:
        return True
    else:
        return False


for i in range(2,n):
    x,y,z=a[i-2],a[i-1], a[i]
    if f(x)==True and f(y)==True or f(z)==True and f(y)==True or f(x)==True and f(z)==True :

        cnt+=1
        b=max(x,y,z)

        mx.append(b)
ans=sum(mx)
print(cnt, ans)
