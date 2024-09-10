#•	Comprueba si 'a' es mayor que 'b' o si 'c' es igual a 'd', pero no ambas condiciones:.

a, b, c, d = 7, 5, 3, 3

Cond1 = a > b
Cond2 = c == d

Solucion = (Cond1 or Cond2) and not (Cond1 and Cond2)

print(Solucion)