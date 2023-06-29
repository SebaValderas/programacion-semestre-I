### LABORATORIO 3, EJERCICIO 1###
s8= 23890
s10=48583
h8=1556805
h10=828708

regiones= {
    "8": "Región del Bio Bio",
    "Superficie Región 8": s8,  
    "Habitantes Region 8": h8,
    "10": "región de Los lagos",
    "Superficie Región 10": s10,
    "Habitantes Región 10": h10
    }
print(regiones)

d8= float(h8/s8)
d8= round(d8,1)
d10= float(h10/s10)
d10= round(d10,1)

print(d8)
print(d10)
regiones["Densidad región 8"]=d8
regiones["Densidad región 10"]=d10
print(regiones)

regiones["Capital región 10"]= "Puerto Montt"
regiones["capital Región 8"]= "Concepción"

comunas8 = ["Lota", "Lebu", "Los Angeles"]
comunas10 = ["Osorno", "Castro", "Puerto Varas"]
regiones["Comunas Región 8"]= comunas8
regiones["Comunas Región 10"]= comunas10

provincias8= ("BioBio", "Arauco", "Concepción")
provincias10= ("Osorno", "Llanquihue", "Chiloé", "Palena")
regiones["Provincias región 8"]= provincias8
regiones["Provincias Región 10"]= provincias10
print(regiones)
















