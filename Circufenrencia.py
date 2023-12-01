import math

def calcular_circunferencia(radio):
    # Utilizamos el valor de pi con 6 decimales
    pi = round(math.pi, 6)
    
    # Calculamos la circunferencia usando la fórmula C = 2 * pi * r
    circunferencia = 2 * pi * radio
    
    return circunferencia

# Definimos los radios
radios = [3, 8, 10]

# Calculamos y mostramos las circunferencias
for radio in radios:
    resultado = calcular_circunferencia(radio)
    print(f"Para un radio de {radio}, la circunferencia es: {resultado}")
