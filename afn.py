class AFN:

  def __init__(self, parser):
    self.parser = parser
    self.logs = []
    self.errors = []
    self.accepted = False
    pass

  def run(self, actualState, string, index, historic):

    # Caso especial quando existe um epsilon no caso estado inicial
    destinationsEpsilon = self.parser.transistions[(actualState, 'epsilon')] if (actualState, 'epsilon') in self.parser.transistions else []   
    if (len(historic) == 1 and len(destinationsEpsilon) > 0):
      for destEp in destinationsEpsilon:
        self.run(destEp, string, index, [destEp])

    # A cadeia foi toda processada e o estado atual é o final, portanto, a cadeia foi aceita
    if (len(string) == index and actualState in self.parser.finals):
      print ("Cadeia aceita: ", string)
      print ("Caminho: ", historic, "\n")
      self.accepted = True
      return

    # Chegou no final da cadeia e não está no e não é o estado final, portanto, cadeia rejeitada
    if (len(string) == index):
      print("Cadeia rejeitada: ", string)
      print("Caminho: ", historic, " \n")
      self.errors.append((string[0:index], historic))
      return

    # Lista dos próximos possíveis estados
    destinations = self.parser.transistions[(actualState, string[index])] if (actualState, string[index]) in self.parser.transistions else [] 

    # Debug
    # print(actualState, ",", string[index], ": ", destinations)

    # Não tem mais caminhos a seguir, portanto, caide arejeitada
    if (len(destinations) == 0):
      print("Cadeia rejeitada: ", string)
      print("Caminho: ", historic, "\n")
      self.errors.append((string[0:index+1], historic))
      return

    # Definir posição para leitura do próximo valor
    nextIndex = index + 1
    
    # Seguir para o(s) próximo(s) estados possíveis
    for dest in destinations:
      self.run(dest, string, nextIndex, historic + [dest])

    # Seguir para o(s) próximo(s) estados possíveis no caso especial de epsilon
    for dest in destinations:
      destinationsEpsilon = self.parser.transistions[(dest, 'epsilon')] if (dest, 'epsilon') in self.parser.transistions else []   
      for destEp in destinationsEpsilon:
        self.run(destEp, string, nextIndex, historic + [dest, destEp])
