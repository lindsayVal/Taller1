suma=0
termino=1
error=1

while error > 0.1:
    suma += termino
    termino /= 2
    error = abs(2-suma)
    print ("sumatoria = ", suma)

print("error_absoluto = ", error)
