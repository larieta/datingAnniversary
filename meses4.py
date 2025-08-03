import os
import time
import webbrowser


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

    print("Eu fiz esse little joguinho aqui pra vc revisitar\nalguns dos nossos melhores dias!!!💚💙")
    print("")
    time.sleep(1)
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
    

def toProntoNao():
    print("")
    print("Negócio de não, tá sim! Vou te explicar como vai funcionar!!🌟")
    input()
    print("")
    instrucoes()

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

def voltarParaEscolherMemoriasOuFim():
    print("Você quer continuar jogando?")

# region funções das memórias
def memoria01():
    print("Memória 01🍓\n")
    print("Dicas da memoria 1")
    print("E aí? Já tá sabendo qual memória é essa? Espero que sim🌟")
    input()
    print("PQ AGORA VOCÊ VAI ESCOLHEEEER💙")
    time.sleep(1)
    print("Opções 1 2 3🌟")
    input()

    
    while True:
        opcaoMemoria01 = input("Qual opção vc acha que é?\n *1, 2 ou 3 viu amor kkkk\n") #usar numeros pelo amor de deus

        match opcaoMemoria01:
            case "1":
                print(" \n...")
                time.sleep(2)

                print("Acertou, meu amor!!!")
                time.sleep(1)
                print("Foi o dia que a gente foi pro Museu da Fotografia pela 1° vez!!")
                print("Tome aqui seu prêmio📸")
                time.sleep(6)

                linkPremio01 = "https://drive.google.com/file/d/1c73g5DBN36F4Bj1unjxKpDPKFa0DNjDW/view?usp=sharing"
                webbrowser.open(linkPremio01)

                time.sleep(3)
                print("🌟")
                input()
                break

            case "2":
                print(" \n...")
                time.sleep(2)
                print("Resposta errada, amor💔 Vai ter que me dá outro beijo pra continuar🌹")
                input()

            case "3":
                print(" \n...")
                time.sleep(2)
                print("Resposta errada, amor💔 Vai ter que me dá outro beijo pra continuar🌹")
                input()
            case _:
                respostaInvalida()

    


def memoria02():
    print("Memória 02🍓\n")
    print("Dicas da memoria 2")
    print("E aí? Já tá sabendo qual memória é essa? Espero que sim🌟")
    input()
    print("PQ AGORA VOCÊ VAI ESCOLHEEEER💙")
    time.sleep(1)
    print("Opções 1 2 3🌟")
    input()

    
    while True:
        opcaoMemoria02 = input("Qual opção vc acha que é?\n *1, 2 ou 3 viu amor kkkk\n") #usar numeros pelo amor de deus

        match opcaoMemoria02:
            case "1":
                print(" \n...")
                time.sleep(2)

                print("Acertou, meu amor!!!")
                time.sleep(1)
                print("titulo da memoria")
                print("Tome aqui seu prêmio📸")
                time.sleep(6)
                
                linkPremio02 = "https://drive.google.com/file/d/1UGgQlHcsiFARnE6MtFHGpcX-8YIDTGum/view?usp=drive_link"
                webbrowser.open(linkPremio02)

                time.sleep(3)
                print("🌟")
                input()
                break

                
                # escolher voltar para as memorias ou acabar o jogo
                #fazer função que pergunta se quer voltar pro menu de escolher memorias ou acabar o jogo
            case "2":
                print(" \n...")
                time.sleep(2)
                print("Resposta errada, amor💔 Vai ter que me dá outro beijo pra continuar🌹")
                input()

            case "3":
                print(" \n...")
                time.sleep(2)
                print("Resposta errada, amor💔 Vai ter que me dá outro beijo pra continuar🌹")
                input()
            case _:
                respostaInvalida()

def memoria03():
    print("Memória 03🍓\n")
    print("Dicas da memoria 2")
    print("E aí? Já tá sabendo qual memória é essa? Espero que sim🌟")
    input()
    print("PQ AGORA VOCÊ VAI ESCOLHEEEER💙")
    time.sleep(1)
    print("Opções 1 2 3🌟")
    input()

    
    while True:
        opcaoMemoria03 = input("Qual opção vc acha que é?\n *1, 2 ou 3 viu amor kkkk\n") #usar numeros pelo amor de deus

        match opcaoMemoria03:
            case "1":
                print(" \n...")
                time.sleep(2)

                print("Acertou, meu amor!!!")
                time.sleep(1)
                print("titulo da memoria")
                print("Tome aqui seu prêmio📸")
                time.sleep(6)
                
                linkPremio03 = "link3"
                webbrowser.open(linkPremio03)
                # region parei aqui
                # endregion parei aqui 

                time.sleep(3)
                print("🌟")
                input()
                break

                
                # escolher voltar para as memorias ou acabar o jogo
                #fazer função que pergunta se quer voltar pro menu de escolher memorias ou acabar o jogo
            case "2":
                print(" \n...")
                time.sleep(2)
                print("Resposta errada, amor💔 Vai ter que me dá outro beijo pra continuar🌹")
                input()

            case "3":
                print(" \n...")
                time.sleep(2)
                print("Resposta errada, amor💔 Vai ter que me dá outro beijo pra continuar🌹")
                input()
            case _:
                respostaInvalida()

def memoria04():
    print("memoria 04")

def memoria05():
    print("memoria 05")


def escolherMemoria():
    while True:
        escolhendoMemoria = input("Qual memória você vai querer?\n" \
                            "(do 1 ao 5)\n")
        match escolhendoMemoria:
            case "1":
                memoria01()
                voltarParaEscolherMemoriasOuFim()
                #se escolher fim break isso aqui e depois break o while principal e vai pro fim
                #se escolher não aí so volta pra ca pra escolher ENTÃO N COLOCA BREAK AQUI NAS MEMORIAS 
                #LEMBRA SE VAI SER NECESSÁRIO COLOCAR BREAK AQUI OU NÃO
            case "2":
                memoria02()
                voltarParaEscolherMemoriasOuFim()
            case "3":
                memoria03()
                voltarParaEscolherMemoriasOuFim()
            case "4":
                memoria04()
                voltarParaEscolherMemoriasOuFim()
            case "5":
                memoria05()
                voltarParaEscolherMemoriasOuFim()
            case _:
                respostaInvalida()
                voltarParaEscolherMemoriasOuFim()
# endregion funções das  memórias

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
