import random

vector1 = [3, 2, 5, 8, 4, 1]

for i in range(len(vector1)):
    for j in range(len(vector1)-i-1):
        if vector1[j] > vector1[j+1]:
            aux = vector1[j]
            vector1[j] = vector1[j+1]
            vector1[j+1] = aux
            
print("vector1 ordenado =", vector1)

#Casos de prueba

vector2 = [-1, 0, 4, 5, 6, 7]

for i in range(len(vector2)):
    for j in range(len(vector2)-i-1):
        if vector2[j] > vector2[j+1]:
            aux = vector2[j]
            vector2[j] = vector2[j+1]
            vector2[j+1] = aux
            
print("vector2 ordenado =", vector2)

vector3=[]

for x in range(100000):
    numero = random.randint(-200, 145)
    vector3.append(numero)
    
print("vector3 =", vector3)
    
for i in range(len(vector3)):
        for j in range(len(vector3)-i-1):
            if vector3[j] > vector3[j+1]:
                aux = vector3[j]
                vector3[j] = vector3[j+1]
                vector3[j+1] = aux

print("\nvector3 ordenado =", vector3)