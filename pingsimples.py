#importa o modulo OS (biblioteca de recursos de sistema operacional)
import os 

print('#'*60) 

#cria variável para receber do usuário o IP
ip_ou_host = input('Digite o IP ou HOST a ser verificado: ')

print('-'*60)

#chamando o módulo System da biblioteca OS - comando ping
#-n(numero de pacotes) qie será 6 e o IP atribuído dentro das chaves com o .format
os.system('ping -n 6 {}'.format(ip_ou_host))

print('-'*60)