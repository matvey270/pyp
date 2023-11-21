def f(a):
    for x in range (1000):
        if not(int(x%33)==0 <= (int(x%45!=0) <= int(x%a!=0))):
            return False
        return True
a=1 
while not f(a):
    a+=1
print(a)
