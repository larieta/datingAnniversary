import os
import time

# region definindo as funções tudo

#==função que ele disse que iniciou
def apresentacaoInicial():
    time.sleep(1)
    print("Pra iniciar vai ter que me da um beijinho🌹")
    input()

    print("Oi, amor da minha vida!!!")
    time.sleep(1)
    print("Em celebração aos nossos 11 MESES...")
    print(" ")
    time.sleep(1)
    print("TCHARAM")
    print(" ")
    time.sleep(1)

    print("Eu fiz esse little coisa aqui pra vc revisitar\nalguns dos nossos melhores dias!!!")
    print("")
    time.sleep(1)
    print("ONZE deles 💚💙")
    print("")
    print("*outro beijinho🌹")
    input()

def estrelinhaSignificaEnter():
    print("Toda vez que aparecer uma '🌟' significa que vc\n" \
    "vai precisar apertar enter pra continuar")
    print("🌟")
    input()
    print("")
def instrucoes():
    print("Eu selecionei 11 memórias que a gente viveu nesses nossos 11 meses de namoro!\n"
          "Aí, vai funcionar assim:\n \n"
          "1. Eu te dou algumas little dicas sobre essa mémória e\n"
          "2. Você☝️ vai descobrir que memória é essa para que depois\n" \
          "3. Você escolha a palavra que mais tem a ver com ela!!!!")
    print(" ")
    print("Alright?🌟 ")
    input()
    print(" \n ")
    print("SE você acertar...BOOM, lhe darei uma lembrancinha🍰\n ")
    print("Se errar...vai ter que me dá outro beijinho pra eu te dar outra chance🌟")
    input()

def respostaInvalida():
    print("")
    print("Meu little código não reconheceu seu texto...💔\nTenta dnv")
    print("")
#==definindo o diabo das funções se ele tá pronto ou não

def toProntoSim():
    print("")
    print("LETS'GO")
    print("")
    print("")
    instrucoes()
    

def toProntoNao():
    print("")
    print("Negócio de não, tá sim! Vou te explicar como vai funcionar!!🌟")
    input()
    print("")
    instrucoes

def taProntoPraIniciar():
    while True:
        toProntoResposta = input("Tá PRONTO? (responde💫)\n").lower()

        match toProntoResposta:
            case "yes" | "sim" | "aham":
                toProntoSim()
                break
            case "não" | "no" | "nop" | "nananinanão" | "nao" | "nops" | "nananinanao":
                toProntoNao()
                break
            case _:
                respostaInvalida()


def escolherMemoria():
    print("Qual memória você vai querer?\n" \
          "(do 1 ao 11\n)")

def fim():
    print("")
# endregion das funções

apresentacaoInicial()
estrelinhaSignificaEnter()
time.sleep(1)

while True:
    respostaInicioOuRetorno = input("Meu amor, você tá iniciando (começo) ou quer ir\n"
                                    "pra uma memória especifica (retorno)?\n").lower()
    match respostaInicioOuRetorno:
        case "começo" | "comeco" | "início":

            print("Vamos começar!!!🌟")
            input()
            instrucoes()
            taProntoPraIniciar()
            escolherMemoria()
            break
        case "retorno" | "específica" | "memória específica":
            print("")
            print("Ok, ok! Memória específica será então!!!🌟")
            input()
            print("")
            escolherMemoria()
            break #LEMBRA DESSE BREAK AQUI CASO TUDO ESTEJA DANDO ERRADO 🌟🌟🌟🌟
        case _: 
            respostaInvalida()
            
fim()





#agora vou perguntar se ele tá pronto ou não




# pergunta qual mês ele vai querer (função gigante com 11 mil casos)  
#chamar as funções dos meses 
#se ele escolher fim agora vou mostrar o textinhoo fofo de fim e fechar o programa!!!!