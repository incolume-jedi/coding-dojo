def weekday(dia: str, qtd: int) -> str:
    dias = ['domingo','segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado']

    for i in range(len(dias)):
        #print(dias[i]) 
        if dia == 'domingo':
            print('segunda-feira')



if __name__ == '__main__':
    weekday('domingo', 1)       