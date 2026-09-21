def algoritmo_aditivo(
    semillas: list[int], m: int, iteraciones: int, k: int = 1
):
    """Genera números pseudoaleatorios mediante el método congruencial aditivo.

    Fórmula: X_{i+1} = (X_i + X_{i-k}) mod m
    R_i = X_{i+1} / m
    `k` es la distancia hacia atrás respecto al último elemento.
    """
    secuencia = list(semillas)
    resultados = []

    for i in range(1, iteraciones + 1):
        # x_i es el último elemento generado; x_{i-k} está a 'k' posiciones más atrás
        siguiente_x = (secuencia[-1] + secuencia[-1 - k]) % m
        r = siguiente_x / m

        secuencia.append(siguiente_x)
        resultados.append((i, siguiente_x, r))

    return resultados


# Ejemplo de uso
semillas = [12, 35]  # x_0 = 12, x_1 = 35
m = 100
num_iter = 6
k = 1  # Para sumar los dos últimos elementos inmediatos

print("--- Algoritmo Congruencial Aditivo ---")
for iteracion, x_val, r_val in algoritmo_aditivo(semillas, m, num_iter, k):
    print(f"Iteración {iteracion}: x_{iteracion+1} = {x_val}, R_{iteracion+1} = {r_val}")