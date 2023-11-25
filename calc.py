def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input
    if operation == '+':
        result=callback(num1,num2)
    elif operation == '-':
        result= callback(num1,num2)
    elif operation == '*':
        result=callback(num1,num2)
    elif operation == '/':
        result=callback(num1,num2)
    else:
        result = "Operacion invalida"
    
    print("Resultado:", result)

def main():
    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")
        #Diccionario con las operaciones y su respectiva funcion lambda
        operations = {"+" : lambda a,b: a+b , "-": lambda a , b : a-b,"/":lambda a , b : a/b,"*":lambda a , b : a*b}

        if user_input[2] in operations:
            #Busca la llave de la operacion respectiva y le pasa como callback a la funcion ejecutar operaciones la operacion
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o  escriba 'exit' para salir.")

if __name__ == "__main__":
    main()
