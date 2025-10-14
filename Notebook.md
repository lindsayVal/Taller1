# Taller 1
## Ejercicio 1
### La sumatoria $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots$ tal que el error absoluto $e_{abs} < 10^{-1}$ 
```python
suma=0
termino=1
error=1

while error > 0.1:
    suma += termino
    termino /= 2
    error= abs(2-suma)
    print ("sumatoria = ", suma)

print("error_absoluto = ", error)
```
## Ejercicio 2
### Implementar el algoritmo de Bubble Sort

Vector Inicial:

$v_1 = [3, 2, 5, 8, 4, 1]$

### Corrida de Escritorio

| i |        Vector         |
|---|-----------------------|
| 0 |  [3, 2, 5, 8, 4, 1]   |
| 1 |  [2, 3, 5, 8, 4, 1]   |
| 2 |  [2, 3, 5, 4, 8, 1]   |
| 3 |  [2, 3, 5, 4, 1, 8]   |
| 4 |  [2, 3, 4, 5, 1, 8]   |
| 5 |  [2, 3, 4, 1, 5, 8]   |
| 6 |  [2, 3, 1, 4, 5, 8]   |
| 7 |  [2, 1, 3, 4, 5, 8]   |
| 7 |  [1, 2, 3, 4, 5, 8]   |

**Resultado Final:**
$V_1 = [1, 2, 3, 4, 5, 8]$

Casos de Prueba

$v_2 = [-1, 0, 4, 5, 6, 7]$

$v_3 =$ 100 000 números aleatorios entre -200 y 145

### Implementación:

```python
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

```

## Ejercicio 3
### Implementar el código de la serie Fibonacci
| n | fib(n) |
|---| --     |
| 0 |   0    |
| 1 |   1    |
| 2 |   1    |
| 3 |   2    |
| 4 |   3    |
| 5 |   5    |
| 6 |   8    |
| 6 |   13   |
| ..| ...    |
|$n = 11 $ | ? |
|$n = 84 $ | ? |
|$n = 1531$| ? |

### Graficar el valor del cociente
| n | $ fib(n) /fib(n-1) $ |
| --| --       |
| 2 | $1/1=1 $ |
| 3 | $2/1 = 2$ |
| 4 | $3/2 = 1.5$ |
| 5 | $5/3= 1.66667$ |
| 6 | $8/5= 1.6$ |
| 7 | $13/8 = 1.625 $ |
| 8 | $21/13 = 1.615 $ |
| ... | ... |
|$\infty $ | $ \frac{1 + \sqrt{5}} {2} \approx 1.618$ (número áureo) |

### Implementación:

```python
import pandas as pd
import matplotlib.pyplot as plt

def fib(n):
    a=0
    b=1

    if n<0:
        print("invalido")

    elif n == 0:
        return a
    
    elif n == 1:
        return b
    
    else:

        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c

        return b

print("Fibonacci de 11 =", fib(11))
print("Fibonacci de 84 =", fib(84))
print("Fibonacci de 1531 =", fib(1531))



valores_n = []
cocientes = []

for n in range (2, 20):
    cociente = fib(n) / fib(n-1)
    valores_n.append(n)
    cocientes.append(cociente)

#cocientes
df = pd.DataFrame({
    "n": valores_n,
    "fib(n)/fib(n-1)":cocientes
})

print("\nCocientes de la serie Fibonacci")
print(df)

df.plot(x="n", y="fib(n)/fib(n-1)", marker="o", legend=False)
plt.axhline(1.618, color="red", linestyle="--", label="Numero aureo ? 1.618")
plt.title("Cociente de la serie Fibonacci")
plt.xlabel("n")
plt.ylabel("fib(n)/fib(n-1)")
plt.legend()
plt.grid()
plt.show()

```
