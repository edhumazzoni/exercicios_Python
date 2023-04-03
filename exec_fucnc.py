def premiacao():
    sorteio = int(input('escolha um número de 1 a 9 para saber seu premio'))
    premio = ['RS 500,00', 'Uma Viagem para a praia', 'Um vale zé de 300 reais', '500 reais no outback', '1 kit perfumes','2 dias de folga', 'Um fim de semana no spa', 'Um vale balada 1000 reais', ' Um fim de semana na praia']
    print(f'Parabens {imprime_nome()}! você ganhou {premio[sorteio-1]} ')
    
    
def imprime_nome():
    nome=str(input('Digite seu nome para sabermos quem é você  '))
    print(nome)
    

def soma():
    total=0
    for dias in range(7):
        print (f"digite o valor dos dias {dias+1}")
        vendas=int(input())
        total=total+vendas
    print(f"total de vendas da semana é de: {total} ")



if soma() < 1000:
    print("meta da semana não atendida")
elif soma() <= 5000:
    print("meta da semana atendida")
elif soma() > 5000:
    print('você merece um premio')
    premiacao()