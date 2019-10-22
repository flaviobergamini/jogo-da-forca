#Alura -- Avançando na linguagem
import os
import random
import time

palavra_secreta = ''
tam = 0
palavra = []

def menu():
   os.system('clear')
   print("+-----------Jogo da forca-------------+")
   print("|                                     |")
   print("| (1) - Inserir palavra chave         |")
   print("| (2) - Exibir palavras cadastradas   |")
   print("| (3) - Jogar                         |")
   print("| (4) - Sair                          |")
   print("+-------------------------------------+")
   receive = input("Entre com o numero: ")

   if(receive == '1' or receive == '2' or receive == '3' or receive == '4'):   
       if receive == '1':
           write_file()
       elif receive == '2':
           arquivo = open("palavras.txt", "r")
           print(arquivo.read())
           input('Pressione Enter para continuar...')
           menu()
       elif receive == '3':
           jogar()
       elif receive == '4':
           exit()
   else:
        print('Opção inválida!')
        time.sleep(1)
        menu()

def jogar():

    palavra_secreta = file_read()
    tam = int(len(palavra_secreta))
    palavra = []
    for i in range(tam):
        palavra.append('-')
    print(palavra)
    erro = 0

    while(True):
        
        chute = input("Qual letra? ").upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):

                    print("Letra {} encontrada na posição {}".format(letra, index))
                    palavra[index] = letra
                index = index + 1
            print(palavra)
        else: 
            erro = erro + 1

        if erro == tam:
            print('---------------------')
            print(" Não foi dessa vez!")
            print('---------------------')
            time.sleep(2)
            menu()

        cont = 0
        for i in range(tam):
            if(palavra[i] != '-'):
                cont = cont + 1
        if(cont == tam):
            print('-----------------------------')
            print("  Parabéns, você ganhou!!!")
            print('-----------------------------')
            time.sleep(2)
            menu()
        else:
            cont = 0
        

def write_file():
    os.system('clear')
    print('---------------Inserir palavra chave------------------')
    palavra_secreta = input("Qual é a palavra secreta? ")

    try:
        arquivo = open('palavras.txt', 'a')
    except:

        arquivo = open('palavras.txt', 'w')
    
    arquivo.write(palavra_secreta)
    arquivo.write('\n')
    arquivo.close()
    menu()


def file_read():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

if (__name__ == "__main__"):
    menu()

