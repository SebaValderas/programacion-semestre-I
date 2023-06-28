print("Tienda de perifericos ofrece:")
print("Teclado mecánico: $50.000")
print("Mouse gamer: $35.000")
print("Mousepad gamer: $18.000")
print("Headset: 80.000")

def desglose():
    precio = int(input("Ingrese el valor del producto: "))
    pago = int(input("Ingrese con cuanto dinero pagará: "))
    if precio>pago:
        print("Valor ingresado es invalido.")
    vuelto = pago - precio
    int(vuelto)
    print(" Vuelto total: ", vuelto)
    diez_k= vuelto // 10000
    vuelto= vuelto % 10000
    print("billetes de $10.000: ",diez_k)

    cinco_k=vuelto // 5000
    vuelto= vuelto %5000
    print("Billetes de $5.000: ",cinco_k)

    dos_k=vuelto // 2000
    vuelto= vuelto % 2000
    print("Billetes de $2.000: ", dos_k)

    luca= vuelto //1000
    vuelto= vuelto % 1000
    print("billetes de $1.000: ", luca)

    quinientos = vuelto // 500
    vuelto = vuelto % 500
    print("Monedas de $500: ", quinientos)

    cien = vuelto // 100
    vuelto = vuelto %100
    print("Monedas de $100: ",cien)

    cincuenta = vuelto // 50
    vuelto = vuelto % 50
    print("Monedas de $50: ",cincuenta)

    diez= vuelto // 10
    vuelto = vuelto % 10
    print("Monedas de $10: ",diez)

desglose()


