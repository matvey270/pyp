def f(x,y,z,w):
    return((w <= (y==z)) or (y == (z<=x)))
print('x y z w')
for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                if f(x,y,z,w):
                    print(x,y,z,w)