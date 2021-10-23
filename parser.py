class Parser:

  def __init__(self, inputfile):
    self.alphabet = []
    self.states = []
    self.initial = ""
    self.finals = []
    self.transistions = {}
    self.read(inputfile)

  def read(self, inputfile):
    with open(inputfile, "r") as file:
      for line in file.readlines():
        if "alfabeto" in line:
          self.alphabet = line.split("=")[1].rstrip("\n").split(",")
        elif "estados" in line:
          self.states = line.split("=")[1].rstrip("\n").split(",")
        elif "inicial" in line:
          self.initial = line.split("=")[1].rstrip("\n")
        elif "finais" in line:
          self.finals = line.split("=")[1].rstrip("\n").split(",")
        elif "transicoes" in line:
          self.isTransition = True
        elif self.isTransition:
          transistion = line.rstrip("\n").split(",")
          print(transistion)
          source = transistion[0]
          dest = transistion[1]
          edge = transistion[2]
          if (source, edge) in self.transistions:
            self.transistions[(source, edge)] = self.transistions[(source, edge)] + [dest]
          else:
            self.transistions[(source, edge)] = [dest]

  def show(self):
    print("Alphabet: {}".format(self.alphabet))
    print("States: {}".format(self.states))
    print("Initial: {}".format(self.initial))
    print("Finals: {}".format(self.finals))
    print("Transitions: {}".format(self.transistions))