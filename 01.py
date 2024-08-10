
zest_1 = [5,10,15,20]
zest_2 = [2,4,6,8]
zest_3 = [0,0,0,0]

licz = 0
for zmi in zest_3:
    zest_3[licz] = zest_1[licz]**2 + zest_2[licz]**2
    licz = licz + 1
    
print(zest_3)

xd = zest_3[0] + zest_3[1] + zest_3[2] + zest_3[3]
xd1 =xd**0.5
print('xd =',xd)
print('xd1 =',xd1)
