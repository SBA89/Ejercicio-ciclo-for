
Total = 0
cons_Riego_papa = 3
cons_Riego_yuca = 1
cons_Riego_zanahoria = 2

opcionInt = int(input('<<< Seleccione su producto >>>\n\n1. Papa\n2. Yuca\n3. Zanahoria\n-->  '))
if opcionInt == 1:
    for i in  range(cons_Riego_papa):
        LitroInt = int(input('Ingrese la cantidad de litros de agua por cosnumir\n-> '))
        Total += LitroInt
    print(f'La cantidad de litros de agua que se consume la Papa a la semana es {Total}')

if opcionInt == 2:
    for i in range(cons_Riego_yuca):
        LitroInt = int(input('Cantidad de litros de agua ingresados\n-> '))
        Total += LitroInt
    print(f'La cantidad de litros de agua que se consume la Yuca a la semana es {Total} ')

if opcionInt == 3:
    for i in range(cons_Riego_zanahoria):
        LitroInt = int(input('Cantidad de litros de agua ingresados\n-> '))
        Total += LitroInt
    print(f'La cantidad de litros de agua que se concume la Zanahoroia a la semana es {Total}  ')
        
        
        