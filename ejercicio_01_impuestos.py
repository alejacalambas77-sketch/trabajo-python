print("Hola , ADSO3229426")

salario = float(input("Ingrese su salario mensual en COP: "))
porcentaje = 0 

if salario >= 12000000 and salario <= 15000000:
    porcentaje = 0.03  
elif salario > 15000000 and salario <= 20000000:
    porcentaje = 0.05  
elif salario > 20000000 and salario <= 30000000:
    porcentaje = 0.08  
elif salario > 30000000:
    porcentaje = 0.10  
else:
    porcentaje = 0  
    
    # Si gana menos de 12 millones, no paga impuesto
    
impuesto_a_pagar = salario * porcentaje

if porcentaje > 0:
    print(f"\nTu salario es de: ${salario:,.2f}")
    print(f"Te corresponde una tasa de impuesto del: {int(porcentaje * 100)}%")
    print(f"El total del impuesto a pagar es: ${impuesto_a_pagar:,.2f}")
else:
    print(f"\nTu salario es de: ${salario:,.2f}")
    print("No debes pagar impuesto tributario.")
    
