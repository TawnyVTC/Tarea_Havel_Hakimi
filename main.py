def teorema(secuencia):
    secuencia = [x for x in secuencia if x != 0]
    
    if not secuencia:
        return True
    
    secuencia.sort(reverse=True)
    degree = secuencia.pop(0)
    
    if degree > len(secuencia):
        return False
    
    for i in range(degree):
        secuencia[i] -= 1
    
    return teorema(secuencia)

# Pedir al usuario el número de vértices
v = int(input("Ingrese el número de vértices: "))

# Pedir al usuario los grados de los vértices
grados = []
for i in range(v):
    grado = int(input(f"Ingrese el grado del vértice {i+1}: "))
    grados.append(grado)

r = teorema(grados)

if r:
    print("La secuencia es gráfica.")
else:
    print("La secuencia no es gráfica.")
