def change():
    expense = 23.75
    money = 100
    expense = float(input("Ingresar gasto:" + "\n"))
    money = float(input("Dinero recibido" + "\n"))

    change_total = money - expense
    change_int = int(change_total)
    change_cents = int((change_total - change_int) * 100)

    
    print("\n" + "Vuelto" + "\n")
    print(f"Pesos:\n{change_int}")
    print(f"Centavos:\n{change_cents}")

change()
