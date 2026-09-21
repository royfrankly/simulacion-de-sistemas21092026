def algoritmo_lineal(x0: int, a: int, c: int, m: int, iteraciones: int):
    """Genera números pseudoaleatorios mediante el método congruencial lineal.

    Fórmula: X_{i+1} = (a * X_i + c) mod m
    R_i = X_{i+1} / m
    """
    x = x0
    resultados = []

    for i in range(1, iteraciones + 1):
        x = (a * x + c) % m
        r = x / m
        resultados.append((i, x, r))

    return resultados


# Ejemplo de uso
x0 = 7
a = 5
c = 3
m = 16
num_iter = 3

print("--- Algoritmo Congruencial Lineal ---")
for iteracion, x_val, r_val in algoritmo_lineal(x0, a, c, m, num_iter):
    print(f"Iteración {iteracion}: x_{iteracion} = {x_val}, R_{iteracion} = {r_val}")