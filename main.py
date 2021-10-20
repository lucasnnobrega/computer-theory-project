from parser import Parser
from afn import AFN

parser = Parser("./data/input.txt")
parser.show()

afn = AFN(parser)

while True:
  string = raw_input("Insira a cadeia de caracteres: ")
  print("AQUI")
  afn.run(parser.initial, string, 0)
  print("Erros: {}".format(afn.errors))
  print("Accpeted: {}".format(afn.accepted))


