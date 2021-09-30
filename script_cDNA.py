#!/usr/bin/env python3

import sys #Importa o módulo syspara utilização posterior

DNA = sys.argv[1] #Obtêm o primeiro parâmetro da linha de comando e atribui à variável DNA
n1 = sys.argv[2] #Obtêm o segundo parâmetro da linha de comando e atribui à variável n1
n2 = sys.argv[3] #Obtêm o terceiro parâmetro da linha de comando e atribui à variável n2
n3 = sys.argv[4] #Obtêm o quarto parâmetro da linha de comando e atribui à variável n3
n4 = sys.argv[5] #Obtêm o quinto parâmetro da linha de comando e atribui à variável n4

if isinstance(DNA, str) and n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit(): #Condicional que transforma as variáveis obtidas de str(string) para int (inteiro) e armazena o valor do tamanho da sequência de DNA caso n1, n2, n3 e n4 sejam considerados dígitos e DNA seja considerado string
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    tDNA = len(DNA)
        
    if ((tDNA > n1) and (tDNA > n2) and (tDNA > n3) and (tDNA > n4)): #Condicional que armazena os códons das duas regiões codificantes (CDS) e armazena em uma variável a presença de determinados códons no in[icio ou fim das CDSs
        LeftCDS1=n1-1
        CDS1 = DNA[LeftCDS1:n2]
        startATG1 = "ATG" in CDS1[0:3]

        LeftCDS2=n3-1
        CDS2 = DNA[LeftCDS2:n4]
        EndTAG2 = "TAG" in CDS2[-3:n4]
        ENDTAA2 = "TAA" in CDS2[-3:n4]
        ENDTGA2 = "TGA" in CDS2[-3:n4]
        
        if startATG1 and (EndTAG2 or ENDTAA2 or ENDTGA2): #Condicional que imprime as CDSs concatenadas caso encontre os códons buscados anteriormente
            print(CDS1+CDS2)
        else: #Condicional que alerta um aviso caso os códons não forem encontrados nas regiões esperadas
            print("CDS1 não começa com ATG e/ou CDS2 não termina com TAG, TAA ou TGA")
    else: #Condicional que alerta caso os valores de n1, n2, n3 ou n4 sejam maiores que a sequência de DNA
        print("O valor do(s) parâmetros n1, n2, n3 e/ou n4 é maior do que a sequência de DNA")
else: #Condicional que alerta sobre os erros na inserção dos dados
    print("Houve um erro de digitação. Por favor, insira sua sequência de DNA em seguida os valores do n1, n2, n3 e n4, nessa ordem. Separe os parâmetros por espaços")#
