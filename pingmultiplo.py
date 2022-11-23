import os
import time

with open('hosts.txt') as file:
    dump = file.read()

    #para printar corretamente dentro do for
    dump =  dump.splitlines()

    #for para percorrer arquivos hosts
    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-'*60)

        #módulo system da biblioteca de sistema operacional - comando ping -2 pacotes
        os.system('ping -n 2 {}'.format(ip))
        print('-'*60)
        #tempo de espera em segundos
        time.sleep(2)

    
