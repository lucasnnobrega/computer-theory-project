from parser import Parser
from multiple_inputs import MultipleInputs
from afn import AFN


def ex1():

  parser = Parser("./data/input.txt")
  parser.show()

  afn = AFN(parser)


  while False:
    #string = raw_input("Insira a cadeia de caracteres: ")
    string = input("\n\nInsira a cadeia de caracteres: ")
    print("\n", "AQUI", string, "\n")
    afn.run(parser.initial, string, 0)
    print("Erros: {}".format(afn.errors))
    print("Accpeted: {}".format(afn.accepted))


# Second exemple
def ex2():

  parser = Parser("./data/AFN1/input.txt")
  parser.show()

  multiple_inputs = MultipleInputs("./data/AFN1/strings.txt")
  multiple_inputs.show()

  string = multiple_inputs.get_inputs()

  len_string = len(string)

  afn = AFN(parser)

  while len_string >= 0:
    #string = raw_input("Insira a cadeia de caracteres: ")
    #string = input("\n\nInsira a cadeia de caracteres: ")
    print("\n", "AQUI", string, "\n")
    afn.run(parser.initial, string[len_string-1], 0)
    print("Erros: {}".format(afn.errors))
    print("Accpeted: {}".format(afn.accepted))
    len_string  = len_string - 1 

## third exemple
def ex3():
  parser = Parser("./data/AFN1/input.txt")
  parser.show()

  afn = AFN(parser)


  while False:
    #string = raw_input("Insira a cadeia de caracteres: ")
    string = input("\n\nInsira a cadeia de caracteres: ")
    print("\n", "AQUI", string, "\n")
    afn.run(parser.initial, string, 0)
    print("Erros: {}".format(afn.errors))
    print("Accpeted: {}".format(afn.accepted))


## fouth exemple
def ex4():
  parser = Parser("./data/AFN2/input.txt")
  parser.show()

  afn = AFN(parser)


  while True:
    #string = raw_input("Insira a cadeia de caracteres: ")
    string = input("\n\nInsira a cadeia de caracteres: ")
    print("\n", "AQUI", string, "\n")
    afn.run(parser.initial, string, 0)
    print("Erros: {}".format(afn.errors))
    print("Accpeted: {}".format(afn.accepted))


#ex1()
ex2()
#ex3()
#import pdb
#pdb.set_trace()
#ex4()