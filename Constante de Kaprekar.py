numero = int(input("Digite um número de até 4 dígitos: "))

if numero < 0:
    print("Erro: o número deve ser positivo.")
else:

    if numero > 9999:
        print("Erro: o número deve ter no máximo 4 dígitos.")
    else:

        d1 = numero // 1000
        d2 = (numero // 100) % 10
        d3 = (numero // 10) % 10
        d4 = numero % 10

        cont0 = (d1 == 0) + (d2 == 0) + (d3 == 0) + (d4 == 0)
        cont1 = (d1 == 1) + (d2 == 1) + (d3 == 1) + (d4 == 1)
        cont2 = (d1 == 2) + (d2 == 2) + (d3 == 2) + (d4 == 2)
        cont3 = (d1 == 3) + (d2 == 3) + (d3 == 3) + (d4 == 3)
        cont4 = (d1 == 4) + (d2 == 4) + (d3 == 4) + (d4 == 4)
        cont5 = (d1 == 5) + (d2 == 5) + (d3 == 5) + (d4 == 5)
        cont6 = (d1 == 6) + (d2 == 6) + (d3 == 6) + (d4 == 6)
        cont7 = (d1 == 7) + (d2 == 7) + (d3 == 7) + (d4 == 7)
        cont8 = (d1 == 8) + (d2 == 8) + (d3 == 8) + (d4 == 8)
        cont9 = (d1 == 9) + (d2 == 9) + (d3 == 9) + (d4 == 9)

        muitos_repetidos = (cont0 >= 3) or (cont1 >= 3) or (cont2 >= 3) or (cont3 >= 3) or (cont4 >= 3) or (cont5 >= 3) or (cont6 >= 3) or (cont7 >= 3) or (cont8 >= 3) or (cont9 >= 3)

        if muitos_repetidos:
            print("Erro: o número possui muitos dígitos repetidos.")
        else:
            print("Número informado:", numero)
            print()

            iteracao = 0
            resultado = numero

            while resultado != 6174:
                a = resultado // 1000
                b = (resultado // 100) % 10
                c = (resultado // 10) % 10
                d = resultado % 10

                if a < b:
                    temp = a
                    a = b
                    b = temp
                if a < c:
                    temp = a
                    a = c
                    c = temp
                if a < d:
                    temp = a
                    a = d
                    d = temp
                if b < c:
                    temp = b
                    b = c
                    c = temp
                if b < d:
                    temp = b
                    b = d
                    d = temp
                if c < d:
                    temp = c
                    c = d
                    d = temp

                ndd = a * 1000 + b * 100 + c * 10 + d
                ndc = d * 1000 + c * 100 + b * 10 + a  

                resultado = ndd - ndc
                iteracao = iteracao + 1

                print("Iteração", iteracao, ":", ndd, "-", ndc, "=", resultado)

            print()
            print("Constante de Kaprekar (6174) atingida em", iteracao, "iterações.")