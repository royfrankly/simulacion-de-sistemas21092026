def cuadrados_medios(x0: int, iteraciones: int):
    """Genera números pseudoaleatorios mediante el método de cuadrados medios.

    Eleva el número al cuadrado, ajusta ceros a la izquierda a 2*n dígitos
    y extrae los n dígitos centrales.
    R_i = X_{i+1} / (10^n)
    """
    n = len(str(x0))
    x = x0
    resultados = []

    for i in range(1, iteraciones + 1):
        cuadrado = x**2
        # Relleno con ceros a la izquierda para garantizar 2*n dígitos
        cuadrado_str = str(cuadrado).zfill(2 * n)

        # Extracción de los n dígitos del centro
        inicio = (len(cuadrado_str) - n) // 2
        centro_str = cuadrado_str[inicio : inicio + n]

        x = int(centro_str)
        r = x / (10**n)
        resultados.append((i, x, r))

    return resultados


# Ejemplo de uso
x0 = 5731  # Semilla de n=4 dígitos
num_iter = 6

print("--- Algoritmo de Cuadrados Medios ---")
for iteracion, x_val, r_val in cuadrados_medios(x0, num_iter):
    print(f"Iteración {iteracion}: x_{iteracion} = {x_val:04d}, R_{iteracion} = {r_val}")