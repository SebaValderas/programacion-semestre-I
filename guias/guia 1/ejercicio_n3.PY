
TarifaxHoraDiurna = 12000
TarifaxHoraNocturna = 16000

#Lunes
pagodiario1_1 = TarifaxHoraNocturna
#Martes
pagodiario1_2 = TarifaxHoraNocturna 
#Miercoles
pagodiario1_3 = TarifaxHoraNocturna
#Jueves
pagodiario1_4 = TarifaxHoraDiurna
#Viernes
pagodiario1_5 = TarifaxHoraDiurna

#Martes
pagodiario2_1 = TarifaxHoraNocturna
#Miercoles
pagodiario2_2 = TarifaxHoraNocturna
#Jueves
pagodiario2_3 = TarifaxHoraNocturna
#Domingo
pagodiario2_4 = TarifaxHoraDiurna + 2000

#Miercoles
pagodiario3_1 = TarifaxHoraDiurna
#Jueves
pagodiario3_2 = TarifaxHoraDiurna
#Viernes
pagodiario3_3 = TarifaxHoraDiurna
#Sabado
pagodiario3_4 = TarifaxHoraNocturna
#Domingo
pagodiario3_5 = TarifaxHoraNocturna + 3000

pagosemanal1 = pagodiario1_1 + pagodiario1_2 + pagodiario1_3 + pagodiario1_4 + pagodiario1_5
pagosemanal2 = pagodiario2_1 + pagodiario2_2 + pagodiario2_3 + pagodiario2_4 
pagosemanal3 = pagodiario3_1 + pagodiario3_2 + pagodiario3_3 + pagodiario3_4 + pagodiario3_5


dic = {    "Empleado 1 y pago del dia lunes:": pagodiario1_1, 
           "Empleado 1 y pago del dia martes": pagodiario1_2,
           "Empleado 1 y pago del dia miercoles": pagodiario1_3,
           "Empleado 1 y pago del dia jueves": pagodiario1_4,
           "Empleado 1 y pago del dia viernes": pagodiario1_5,
           "Empleado 2 y pago del dia martes": pagodiario2_1,
           "Empleado 2 y pago del dia miercoles": pagodiario2_2,
           "Empleado 2 y pago del dia jueves": pagodiario2_3,
           "Empleado 2 y pago del dia domingo": pagodiario2_4,
           "Empleado 3 y pago del dia miercoles": pagodiario3_1,
           "Empleado 3 y pago del dia jueves": pagodiario3_2,
           "Empleado 3 y pago del dia viernes": pagodiario3_3,
           "Empleado 3 y pago del dia sabado": pagodiario3_4,
           "Empleado 3 y pago del dia domingo": pagodiario3_5,
           "Pago semanal empleado 1": pagosemanal1,
           "Pago semanal empleado 2": pagosemanal2,
           "Pago semanal empleado 3": pagosemanal3}

print(dic) 

