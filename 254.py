with open('17-243.txt') as l:
    a=[int(i) for i in l]
n=len(a)
cnt=0 
mx=[]
mn=10**9
for i in range(n):

    if a[i]%151==0:
        mx.append(a[i])
g=max(mx)
def f(x):
    x=hex(x)
    po=0
    pl=0
    for i in x:
        if i == '3':

            po+=1
        else:
            pl+=1
    if po>=1:
        return True
    else:
        return False


for i in range(n-1):
    x,y=a[i], a[i+1]
    if f(x)==True and x>g or f(y)==True and y>g or f(x)==True and y>g or f(y)==True and x>g :

        cnt+=1
        mn=min(mn,x+y)

print(cnt, mn)