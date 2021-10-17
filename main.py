import time
from icecream import ic
from multiprocessing import Process

# lista de strings 
alfabeto = []
estados = []
inicial = []
final = []
transicoes = []


def le_arquivos():
    with open("./entrada1.txt", "r") as file:
        for line in file.readlines():
            #print(line)
            ic.disable()
            linha = line.split("#")[0]
            if "alfabeto" in linha:
                ic(linha.split("=")[1])
                aux = linha.replace(" ","").split("=")[1]
                ic(aux.split(","))
                alfabeto = aux.split(",")
            if "estados" in linha:
                ic(linha.split("=")[1])
                aux = linha.replace(" ","").split("=")[1]
                ic(aux.split(","))
                estados = aux.split(",")
            if "inicial" in linha:
                ic(linha.split("=")[1])
                aux = linha.replace(" ","").split("=")[1]
                ic(aux.split(","))
                inicial = aux.split(",")
            if "finais" in linha:
                ic(linha.split("=")[1])
                aux = linha.replace(" ","").split("=")[1]
                ic(aux.split(","))
                final = aux.split(",")
            if "=" not in linha and "transicoes" not in linha:
                aux = linha.replace(" ","")
                ic(aux.split(","))
                transicoes.append(aux.split(","))
                ic(transicoes)

    return alfabeto, estados, inicial, final, transicoes

ic(" ")
alfabeto, estados, inicial, final, transicoes = le_arquivos()
ic.enable()
ic(alfabeto, estados, inicial, final, transicoes)

'''


dfa = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}


def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting

ic(accepts(dfa,0,{0},'1011101'))
ic(accepts(dfa,0,{0},'10111011'))
'''

