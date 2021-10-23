import argparse

from parser import Parser
from multiple_inputs import MultipleInputs
from afn import AFN
from utils import checkStringToAlphabet

# Main function to user input
def main1(inputfile):

  parser = Parser(inputfile)
  parser.show()

  while True:
    string = input("\n\nInsira a cadeia de caracteres: ")
    print("\n")

    if checkStringToAlphabet(parser.alphabet, string) == False:
      print("A cadeia de caracteres contém elementos de fora do alfabeto")
      continue

    afn = AFN(parser)
    afn.run(parser.initial, string, 0, [parser.initial])

    if (afn.accepted):
      print("Cadeia aceita!")
    else:
      print("Cadeia rejeitada!")


# Main function reading from file
def main2(inputfile, stringsfile):

  parser = Parser(inputfile)
  parser.show()

  multiple_inputs = MultipleInputs(stringsfile)
  strings = multiple_inputs.get_inputs()

  for string in strings:
    print("\n\n########################")
    print("Cadeia: ", string, "\n")
    afn = AFN(parser)
    afn.run(parser.initial, string, 0, [parser.initial])
    
    if (afn.accepted):
      print("Cadeia aceita!")
    else:
      print("Cadeia rejeitada!")


# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-m", "--mode", required=True, help="Modo de execução [1: usuário interativo, 2: leitura a partir de arquivo]")
ap.add_argument("-i", "--input", required=True, help="Caminho para o arquivo de input")
ap.add_argument("-s", "--stringsfile", required=False, help="Caminho para o arquivo com as strins")
args = vars(ap.parse_args())

if (args['mode'] ==  '1'):
  main1(args['input'])
else:
  main2(args['input'], args['stringsfile'])