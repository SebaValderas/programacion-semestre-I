#Declaradno tuplas sin parentesis
t = 1, 2, 3
tuplita = "Messi", "Cristiano", "Neymar", "Alexis"

print(type(t))
print(type(tuplita))

jugadores = [("Messi", 15, 18), ("Cristiano", 12, 18), ("Neymar", 14, 20)]
print(jugadores)

for jugador in jugadores:
    print(jugador)

promedios = []

for i in jugadores:
    nombre = i[0]
    goles   = i[1]
    partidos   = i[2]
    promedio = goles/partidos

print(promedios)