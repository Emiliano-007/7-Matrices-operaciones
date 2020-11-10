import numpy as np

a=np.zeros((5,4))
b=np.zeros((5,4))

print('######################################################################')
for x in range(5):
    for y in range(4):
        a1=x
        a1=str(a1)
        b1=y
        b1=str(b1)
        num1=int(input("Dar numero de la matriz 1 posicion "+a1+','+b1+' :'))
        a[x][y]=np.array(num1)
print('######################################################################')
for x in range(5):
    for y in range(4):
        a2=x
        a2=str(a2)
        b2=y
        b2=str(b2)
        num2=int(input("Dar numero de la matriz 2 posicion "+a2+','+b2+' :'))
        b[x][y]=np.array(num2)
print('######################################################################')
print(' ')
print('########################Martriz rellena 1#############################')
print(a)
print('########################Martriz rellena 2#############################')
print(b)
print('########################Suma de matrices##############################')
print(a+b)


