ingreso_mensual = 10000
gasto_mensual = 5000

# if anidados y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas fresco")
    else:
        print("Broder estas en deuda")

if ingreso_mensual > 700:
    print("Puedes comprarte cosas para tu uso")

elif ingreso_mensual >= 400:
    print("Aun puedes comparte cosas para tu uso")

else:
    print("No puedes comprate cosas")
