import math

radio = float(input("Ingrese el radio del círculo: "))

perimetro = 2 * math.pi * radio
area = math.pi * radio ** 2

print(f"Perímetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")