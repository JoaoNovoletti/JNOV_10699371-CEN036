#!/usr/bin/env python3

import sys #Importa o módulo syspara utilização posterior

a = sys.argv[1] #Obtêm o primeiro parâmetro da linha de comando e atribui à variável a (no caso o cateto 1)
b = sys.argv[2] #Obtêm o segundo parâmetro da linha de comando e atribui à variável a (no caso o cateto 2)
if a.isdigit() and b.isdigit(): #Condicional que executa transforma as variáveis obtidas de str(string) para int (inteiro) caso a e b sejam considerados dígitos
    a = int(a)  
    b = int(b) 
    if (a > 0 and b > 0) and (a < 1000 and b < 1000): #Condicional que executa o cálculo da hipotenusa e emite o resultado na tela, caso o número seja positivo e menor que 1000. *Obs.: Não precisaria introduzir a condição de positivo, pois ".isdigit()" não aceita sinais.
        Quadradoa = a**2 
        Quadradob = b**2
        QuadradoHip = Quadradoa + Quadradob
        A=str(Quadradoa) 
        B=str(Quadradob)
        print("O quadrado da hipotenusa para o triangulo retângulo com lados a=" + A + " e b=" + B + " é", QuadradoHip)
    elif (a > 0 and b > 0) and (a >= 1000 and b >= 1000): #Condicional que emite um aviso caso os dois números sejam maiores que 1000
        print("Foram inseridos dois valores interios e positivos, porém ambos são maiores ou iguais a 1000") 
    elif (a > 0 and b > 0) and ((a < 1000 and b >= 1000) or (a >= 1000 and b < 1000)): #Condicional que emite um aviso caso um dos números seja maior que 1000
        print("Foram inseridos dois valores interios e positivos, porém um deles é maior ou igual a 1000") 
    else: #Condicional para caso o valor digitado não se enquadre nas anteriores
        print("Insira dois valores inteiros POSITIVOS menores que 1000")    
elif (a.isdigit() and not b.isdigit()) or (not a.isdigit() and b.isdigit()): #Condicional que emite um aviso caso um dos parâmetros não seja considerado "dígito"
    print("Foi inserido apenas um número inteiro positivo, lembre de digitar dois valores inteiros, positivos e menores que 1000")
else: #Condicional que emite um sinal caso não seja inserido parâmetros considerados "dígitos"
    print("Não foram inseridos números inteiros ou esses não são positivos. Lembre-se devem ser dois valores inteiros, positivos e menores que 1000")
