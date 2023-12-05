n=153
a=''
p=bin(n)[2:]
c=len(p)
g=p[:c-1]
for i in g:
    if i=='1':
        i='0'
    else:
        i='1'
    a+=i
ans=int(a,2)
print(ans)
