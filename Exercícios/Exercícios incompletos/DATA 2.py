#nao vamos colocar os bissextos
#7 meses tem 31, um tem 28 e os outros 4 tem 30
 
i = 1
contadorDias_1 = 0
contadorDias_2 = 0
contadorDiasInicial = 0
 
data1_Dia = int(input("Digite o dia em que você nasceu: "))
data1_Mes = int(input("Digite o mes em que você nasceu: "))
data1_Ano = int(input("Digite o ano em que você nasceu: "))
 
data2_Dia = int(input("\nDigite o dia em que você está: "))
data2_Mes = int(input("Digite o mes em que você está: "))
data2_Ano = int(input("Digite o ano em que você está: "))
 
#quantidade de anos
anos = (data2_Ano - data1_Ano) - 1

## ANO EM QUE A PESSOA ESTÁ ## 
#quantidade de dias no ano em que a pessoa está

while (i < data2_Mes):

    if((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i == 12)):
        contadorDias_1 = contadorDias_1 + 31    

    if((i == 4) or (i == 6) or (i == 9) or (i == 11)):
        contadorDias_1 = contadorDias_1 + 30

    if(i == 2):
        contadorDias_1 = contadorDias_1 + 28
    
    i += 1


contadorDias_1 += data2_Dia

## ANO QUE A PESSOA DIGITOU INICIALMENTE ##
# Contando a quantidade de dias do mês seguinte ao digitado inicialmente até o final do ano
i = (data1_Mes + 1)

while (i <= 12):

    if((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i == 12)):
        contadorDias_2 = contadorDias_2 + 31    

    if((i == 4) or (i == 6) or (i == 9) or (i == 11)):
        contadorDias_2 = contadorDias_2 + 30

    if(i == 2):
        contadorDias_2 = contadorDias_2 + 28
    
    i += 1

i = data1_Mes
# Contando os dias desde a data do dia inicial digitado até o final do mês 1

if((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i == 12)):
        contadorDiasInicial += 31 - data1_Dia     

if((i == 4) or (i == 6) or (i == 9) or (i == 11)):
        contadorDiasInicial += 31 - data1_Dia

if(i == 2):
        contadorDiasInicial += 31 - data1_Dia

#Contador de dias a partir da data em que o usuário digitou inicialmente.

# VERIFICAÇÃO 



contadorDias_2 = contadorDias_2 + contadorDiasInicial

totalDias = (contadorDias_1 + contadorDias_2) + (anos*365)

print(f"Anos de vida {anos}")
print(f"A quantidade de dias entre a data digitada e a data atual é: {totalDias}")
