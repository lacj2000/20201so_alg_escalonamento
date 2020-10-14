import queue


def escalonar_processos(quantum, troca_contexto, processos):
    tempo = 0
    anterior = ''
    print_cabecalho()
    while(not processos.empty()):
        processo = processos.get()

        if processo['inicio'] <= tempo:    
            if(anterior != processo['nome'] and anterior != ''):
                print(tempo,': tc')
                tempo += troca_contexto
            anterior = processo['nome']
           
           
            # print #
            print(tempo, ':', sep=' ', end =' ')
            print_processo(processo)
            if processo['duracao'] > quantum:
                processo['duracao'] -= quantum  
                processos.put(processo)
                tempo += quantum
                # print #
                print(tempo,':', sep=' ', end =' ')
                print_processo(processo)
            elif processo['duracao'] == quantum:  
                tempo += quantum
                print(tempo,': finalizado', processo['nome'], sep=' ')
            else:
                tempo += processo['duracao']
                print(tempo,': finalizado', processo['nome'], sep=' ')
        else:
            processos.put(processo)


def print_processo(processo):
    print(processo['nome'],' | ',processo['inicio'], ' | ',processo['duracao'])


def print_cabecalho():
    print('t : nome |  inicio | Tempo restante')


def organizar_fila(processos):
    processos.sort(key =lambda p: p['inicio'])
    fila_processos = queue.Queue()
    for p in processos:
        fila_processos.put(p);
    return fila_processos

       
if __name__ == '__main__':
    escalonamento = {'quantum':15, 'troca_contexto':5}
    processos = [
        { 'inicio': 30, 'nome':'p2', 'duracao':65},
        { 'inicio': 0, 'nome':'p1', 'duracao':45}
    ]
    fila_processos = organizar_fila(processos)
    escalonar_processos(escalonamento['quantum'],escalonamento['troca_contexto'], fila_processos) 




