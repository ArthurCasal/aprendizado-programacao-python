operadores = ["+", "-", "x", "/"]

while True:
    try:
        num1 = input("Digite o primeiro numero: ")
        num2 = input("Digite o segundo numero: ")
        num1_float = float(num1)
        num2_float = float(num2)  
    except ValueError:
        print('Digite um numero valido')
        continue
       
    operaçao = input("Digite a sua operação[+ - x /]: ")
    operaçao = operaçao.lower()
    if len(operaçao) > 1:
        print("Escolha apenas uma operação")
        continue
    if operaçao in operadores:
        if operaçao == '+':
            resultadoA = num1_float + num2_float
            print(f'A soma entre {num1} e {num2} é: {resultadoA:.2f}')    
        elif operaçao == "-":
            resultadoA = num1_float - num2_float
            print(f'A subtração entre {num1} e {num2} é: {resultadoA:.2f}')          
        elif operaçao == "x":
            resultadoA = num1_float * num2_float
            print(f"A multiplicação entre {num1} e {num2} é: {resultadoA:.2f}")
        elif operaçao == "/":
            if num2_float != 0:
                resultadoA = num1_float / num2_float
                print(f"A divisão entre {num1} e {num2} é: {resultadoA:.2f}")
            else:
                print("Não é possível dividir por zero.")
    else:
        print('Escolha uma operação valida')
    while True:
        print('Deseja fazer outra operação?')
        escolha = input("[S] | [N]\n\n")
        if escolha.upper() == 'S':
            break
        elif escolha.upper() == 'N':
            break
        else:
            print('Digite uma opcão correta')
    if escolha.upper() == 'N':
        break
