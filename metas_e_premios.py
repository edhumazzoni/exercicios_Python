def valores_da_semana():
    dias_da_semana = []
    
    for dias in range(7):
        dias_separados = int(input(f'digite o valor vendido no dia {dias+1} '))
        dias_da_semana.append(int(dias_separados))
    
    return dias_da_semana


def soma(dias):
    total = 0
    
    for venda in dias:
        total = total + venda
        
    return total


def premiacao():
    premios_da_lista = ['equivalente a V1', 'equivalente a V2', 'equivalente a V3', 'equivalente a V4', 'equivalente a V5', 'equivalente a V6', 'equivalente a V7', 'equivalente a V8', 'equivalente a V9']
    num_da_sorte = int(input('escolha um numero entre 1 e 9 '))
    sorteio = premios_da_lista[num_da_sorte-1]
    cagao = "cagção de merda! "
    return num_da_sorte, sorteio, cagao


def metas():
    valores_diarios = valores_da_semana()
    soma_da_semana = soma(valores_diarios)
    if soma_da_semana < 1000:
        print("meta da semana não atendida")
    
    elif soma_da_semana <= 5000:
        print("meta da semana atendida")
    else:
        print('você merece um prêmio')
        return ''
    
    return soma_da_semana


meu_premio = metas()
print(meu_premio)     
  
premio = premiacao()
print(f'parabéns, você escolheu o número {premio[0]} que corresponde a {premio[2]}')