# integrantes
# Hugo Emílio Nomura
# Pedro Henrique Satoru Lima Takahashi
# Vitor Monteiro Vianna
# Paulo Hudson

# Objetivo: Objetivo: Estudo o modelo de Bohr para o átomo de hidrogênio e quantização com programação em linguagem Python.

# Os cálculos no programa devem ser feitos com constantes com 4 algarismos significativos. Indicar a unidade de
# todos os valores de entrada e saída do programa. O usuário pode ser forçado a digitar na unidade indicada ou ter
# opção de digitar na unidade desejada ou escolher de uma lista.
# Os resultados dos cálculos devem ser exibidos com notação científica, com três algarismos significativos, para
# valores muito pequenos ou muito grandes.
# Os valores de entrada e saída do programa que serão avaliados são: número quântico (n), Energia do fóton (Efóton)
# absorvido/emitido, frequência do fóton (f) absorvido/emitido, comprimento de onda do fóton ()
# absorvido/emitido, raio da órbita (rn), velocidade (vn), energia cinética (Kn), energia potencial (Un), energia total (En)
# e comprimento de onda do elétron (n).
from math import *

c=3e8        #velocidade da luz
m=9.11e-31   #massa do eletron
h=6.626e-34  #constante de Planck
h2=4.136e-15 #constante de Planck em eV


texto_inicial = '''Calculadora do modelo de Bohr para o átomo de hidrogênio

DEENVOLVIDO POR:
    -Hugo Emílio Nomura
    -Pedro Henrique Satoru Lima Takahashi
    -Vitor Monteiro Vianna
    -Paulo Hudson

OQUE PODEMOS CALCULAR:
    -Propriedades do Atomo de Hidrogênio
    -Emissão/Absorção de Fótons pelo Hidrogênio 
    -Mesmas Entradas para emisão e absorção
    -Propriedades dos Fotons

'''
def menu():
    print(texto_inicial)
    print("Qual é a sua entrada?")
    #Propriedades do Atomo de Hidrogênio
    print("1 - Número quântico (n)")
    #Emissão/Absorção de Fótons pelo Hidrogênio  # Considere o modelo de Bohr para o átomo de hidrogênio e a série de Lyman. Calcule a frequência do fóton emitido na transição a partir do  nível n = 2. 
    print("2 - Número quântico (n) inicial e final")
    #Mesmas Entradas para emisão e absorção
    print("3 - Numero quântico (n) final e frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    print("4 - Numero quântico (n) inicial e frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    #Fotons
    print("5 - Frequencia do fóton (f), ou comprimento de onda do fóton (λ)")
    print("6 - Energia do fóton (Efóton), em Joule (J) ou em elétron-volt (eV)")
    print("7 - Calcular o maior comprimento de onda da série de Brackett")
    print("8 - Determinar o nível quântico final a partir do comprimento de onda do fóton e do nível quântico inicial")
    print("9 - Calcular o nível quântico final a partir da absorção de um fóton, dado o nível quântico inicial e o comprimento de onda do fóton")
    print("10 - Calcular a frequência do fóton emitido para uma transição específica de estado")
    print("11 - Calcular o comprimento de onda do fóton emitido na transição a partir do 30 nível excitado.")



    escolha=int(input())
    if escolha == 1:
        n_H = float(input("Digite o número quântico (n): "))
        Rn= n_H**2 * 5.29e-11       #Rn é o raio da órbita do eletron no atomo de hidrogenio
        Vn= 2.18e6/n_H              #Vn é a velocidade do eletron no atomo de hidrogenio
        Kn= 13.6/n_H**2             #Kn é a energia cinetica do eletron no atomo de hidrogenio
        Un= -27.2/n_H**2            #Un é a energia potencial do eletron no atomo de hidrogenio
        En= -13.6/n_H**2            #En é a energia total do eletron no atomo de hidrogenio
        λn= h/(m*Vn)                #λn é o comprimento de onda do eletron no atomo de hidrogenio
        print('Rn: {:.2e} m'.format(Rn))
        print('Vn: {:.2e} m/s'.format(Vn))
        print('Kn: {:.2e} eV'.format(Kn))
        print('Un: {:.2e} eV'.format(Un))
        print('En: {:.2e} eV'.format(En))
        print('λn: {:.2e} m'.format(λn))
        

#-------------------------------------------------------------------------------------------------------------------------------#
    elif escolha == 2:
        nInicial=float(input("Digite o número quântico inicial: "))
        nFinal=float(input("Digite o número quântico final: "))
        EnInicial= -13.6/nInicial**2
        EnFinal= -13.6/nFinal**2
        if EnInicial>EnFinal:
            Efóton= abs(EnInicial-EnFinal) #Energia do fóton absorvido
        else:
            Efóton= EnFinal-EnInicial      #Energia do fóton absorvido   
        λ= h2* c/Efóton                    #Comprimento de onda do fóton
        f= Efóton/h2                       #Frequencia do fóton
        print('Ef: {:.2e} eV'.format(Efóton))
        print('λ: {:.2e} m'.format(λ))
        print('f: {:.2e} Hz'.format(f))
        
#-------------------------------------------------------------------------------------------------------------------------------#
    elif escolha == 3:
        nFinal=float(input("Digite o número quântico Final: "))
        opcao1=int(input("Digite 1 para EMISAO ou 2 para ABSORCAO): "))
        #Emisao
        if opcao1==1:
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                EInicial=(-13.6/nFinal**2) + (h2*frequencia)
                nI = round(sqrt(-13.6/EInicial))
                print('nI: ',+nI)
            else:
                λ=float(input("Digite o comprimento de onda do fóton (λ): "))
                EInicial=(-13.6/nFinal**2) + ((h2*c)/λ)
                nI = round(sqrt(-13.6/EInicial))
                print('nI: ',+nI)

        #Absorcao
        else:
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                EInicial=(-13.6/nFinal**2) - (h2*frequencia)
                nI = round(sqrt(-13.6/EInicial))
                print('nI: ',+nI)
            else:
                λ=float(input("Digite o comprimento de onda do fóton (λ): "))
                EInicial=(-13.6/nFinal**2) - ((h2*c)/λ)
                nI = round(sqrt(-13.6/EInicial))
                print('nI: ',+nI)
        
#-------------------------------------------------------------------------------------------------------------------------------#
    elif escolha == 4:
        nInicial=float(input("Digite o número quântico Inicial: "))
        opcao1=int(input("Digite 1 para EMISAO ou 2 para ABSORCAO): "))
        #Emisao
        if opcao1==1:
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                EFinal=(-13.6/nInicial**2) - (h2*frequencia)
                nF = round(sqrt(-13.6/EFinal))
                print('nF: ',+nF)
            else:
                λ=float(input("Digite o comprimento de onda do fóton (λ): "))
                EFinal=(-13.6/nInicial**2) - ((h2*c)/λ)
                nF = round(sqrt(-13.6/EFinal))
                print('nF: ',+nF)
        #Absorcao
        else:
            opcao2=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ): "))
            if opcao2 == 1:
                frequencia=float(input("Digite a frequencia do fóton (f): "))
                EFinal=(-13.6/nInicial**2) + (h2*frequencia)
                nF = round(sqrt(-13.6/EFinal))
                print('nF: ',+nF)
            else:
                λ=float(input("Digite o comprimento de onda do fóton (λ): "))
                EFinal=(-13.6/nInicial**2) + ((h2*c)/λ)
                nF = round(sqrt(-13.6/EFinal))
                print('nF: ',+nF)

#-------------------------------------------------------------------------------------------------------------------------------#
        
    elif escolha == 5:
        escolha4=int(input("Digite 1 para frequencia do fóton (f) ou 2 para comprimento de onda do fóton (λ):"))
        if escolha4 == 1:
            frequencia=float(input("Digite a frequencia do fóton (f) em Hz: "))
            e_foton_joule = h * frequencia
            e_foton_ev = e_foton_joule / 1.6e-19

        else:
            comprimento_de_onda=float(input("Digite o comprimento de onda do fóton (λ) em metros: "))
            e_foton_joule = (h * c) / comprimento_de_onda
            e_foton_ev = e_foton_joule / 1.6e-19

        print('E fóton = {:.2e} J'.format(e_foton_joule))
        print("E fóton = {:.2e} eV".format(e_foton_ev))

#-------------------------------------------------------------------------------------------------------------------------------#      
    elif escolha == 6:
        Escolha5 = int(input("Digite 1 para energia do fóton (Efóton) em Joule (J) ou 2 para elétron-volt (eV): "))
        Efoton=float(input("Digite a energia do fóton (Efóton) na unidade especificada: "))

        if Escolha5 == 2: # Converte eV para J
            Efoton = Efoton * 1.6e-19

                                     # Caso Tenham dois valores:
        f = Efoton / h               # Menor Energia representa menor frequencia. Maior energia representa maior frequencia
        comprimento_de_onda = c / f  # O valor maior representa o menor comprimento visivel, e o menor valor o maior comprimento visivel
        

        print('f = {:.2e} Hz'.format(f))
        print('comprimento de onda (λ) = {:.2e} m'.format(comprimento_de_onda))
#-------------------------------------------------------------------------------------------------------------------------------#  
    elif escolha == 7:
        nInicial = 5
        nFinal = 4
        EnInicial = -13.6 / nInicial**2
        EnFinal = -13.6 / nFinal**2
        Efóton = abs(EnInicial - EnFinal)  # Energia do fóton emitido
        λ = h2 * c / Efóton  # Comprimento de onda do fóton em metros
        λ_nm = λ * 1e9  # Convertendo para nanômetros
        print('O maior comprimento de onda da série de Brackett é: {:.3e} nm'.format(λ_nm))
#-------------------------------------------------------------------------------------------------------------------------------#  
    elif escolha == 8:
        nInicial = float(input("Digite o número quântico inicial: "))
        lambda_foton = float(input("Digite o comprimento de onda do fóton (em nm): "))
        lambda_foton_m = lambda_foton * 1e-9  # Convertendo nm para metros
        
        E_foton = (h * c) / lambda_foton_m  # Energia do fóton em Joules
        E_foton_eV = E_foton / 1.6e-19  # Convertendo energia para eV

        # Resolver para o nível quântico final usando a fórmula de energia
        # -13.6/n_final^2 = -13.6/n_inicial^2 - E_foton_eV
        for nFinal in range(1, int(nInicial)):
            E_nFinal = -13.6 / nFinal**2
            if abs(E_nFinal + 13.6 / nInicial**2) < abs(E_foton_eV):
                print(f"O número quântico final estimado é: {nFinal}")
                break
#--------------------------------------------------------------------------------------------------------------------------------#
    elif escolha == 9:
        nInicial = float(input("Digite o número quântico inicial (n): "))
        lambda_foton = float(input("Digite o comprimento de onda do fóton absorvido (em nm): "))
        lambda_foton_m = lambda_foton * 1e-9  # Convertendo nm para metros
        
        E_foton = (h * c) / lambda_foton_m  # Energia do fóton em Joules
        E_foton_eV = E_foton / 1.6e-19  # Convertendo energia para eV

        # Usar a fórmula de energia para encontrar o nível quântico final após a absorção
        # -13.6/n_final^2 = -13.6/n_inicial^2 + E_foton_eV
        n_final = sqrt(-13.6 / (-13.6 / nInicial**2 + E_foton_eV))
        print(f"Após a absorção do fóton, o elétron transita para o nível quântico: {int(round(n_final))}")
#--------------------------------------------------------------------------------------------------------------------------------#
    elif escolha == 10:
        nInicial = int(input("Digite o nível quântico inicial (n_i): "))
        nFinal = int(input("Digite o nível quântico final (n_f): "))
        EnInicial = -13.6 / nInicial**2
        EnFinal = -13.6 / nFinal**2
        Efóton = abs(EnInicial - EnFinal)  # Energia do fóton emitido em eV
        f = Efóton / h2                    # Frequência do fóton em Hz
        print('A frequência do fóton emitido para a transição de n={} para n={} é: {:.4g} Hz'.format(nInicial, nFinal, f))
#--------------------------------------------------------------------------------------------------------------------------------#       
    elif escolha == 11:
        nInicial = 30  # 30º nível excitado
        nFinal = 4  # Final para a série de Brackett
        EnInicial = -13.6 / nInicial**2  # Energia inicial
        EnFinal = -13.6 / nFinal**2  # Energia final
        Efoton = abs(EnInicial - EnFinal)  # Energia do fóton emitido em eV
        lambda_foton = h2 * c / Efoton  # Comprimento de onda do fóton em metros
        lambda_foton_nm = lambda_foton * 1e9  # Conversão para nanômetros
        print(f"O comprimento de onda do fóton emitido na transição de n={nInicial} para n={nFinal} é: {lambda_foton_nm:.2f} nm")

        # Classificação no espectro eletromagnético
        if lambda_foton_nm < 0.01:
            categoria = "Raios Gama"
        elif lambda_foton_nm < 10:
            categoria = "Raios X"
        elif lambda_foton_nm < 400:
            categoria = "Ultravioleta"
        elif lambda_foton_nm < 700:
            categoria = "Visível"
        elif lambda_foton_nm < 1e6:
            categoria = "Infravermelho"
        elif lambda_foton_nm < 3e8:
            categoria = "Micro-ondas"
        else:
            categoria = "Ondas de Rádio"
        
        print(f"Este fóton é classificado como {categoria} no espectro eletromagnético.")




        
    else:
        print("Opção inválida")
        menu()

menu()