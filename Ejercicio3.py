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
