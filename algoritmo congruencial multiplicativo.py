def algoritmo_multiplicativo(x0: int, a: int, m: int, iteraciones: int):
    """Genera números pseudoaleatorios mediante el método congruencial multiplicativo.

    Fórmula: X_{i+1} = (a * X_i) mod m
    R_i = X_{i+1} / m
    """
    x = x0
    resultados = []

    for i in range(1, iteraciones + 1):
        x = (a * x) % m
        r = x / m
        resultados.append((i, x, r))

    return resultados


# Ejemplo de uso
x0 = 7
a = 5
m = 16
num_iter = 5

print("--- Algoritmo Congruencial Multiplicativo ---")
for iteracion, x_val, r_val in algoritmo_multiplicativo(x0, a, m, num_iter):
    print(f"Iteración {iteracion}: x_{iteracion} = {x_val}, R_{iteracion} = {r_val}")