class AFN:

  def __init__(self, parser):
    self.parser = parser
    self.logs = []
    self.errors = []
    self.accepted = False
    pass

  def run(self, actualState, string, index, historic):

    #special case
    destinationsEpsilon = self.parser.transistions[(actualState, 'epsilon')] if (actualState, 'epsilon') in self.parser.transistions else []   
    if (len(historic) == 1 and len(destinationsEpsilon) > 0):
      for destEp in destinationsEpsilon:
        print(actualState, destinationsEpsilon)
        self.run(destEp, string, index, [destEp])

    # print("Actual state: ", actualState)

    if (len(string) == index and actualState in self.parser.finals):
      print ("Cadeia aceita: ", string, historic)
      self.accepted = True
      return

    if (len(string) == index):
      print ("Cadeia rejeitada: ", string, " - Caminho: ", historic)
      self.errors.append((string[0:index], historic))
      return

    destinations = self.parser.transistions[(actualState, string[index])] if (actualState, string[index]) in self.parser.transistions else [] 
    print(actualState, ",", string[index], ": ", destinations)

    if (len(destinations) == 0):
      print ("Cadeia rejeitada: ", string, " - Caminho: ", historic)
      self.errors.append((string[0:index+1], historic))
      return

    nextIndex = index + 1
    
    for dest in destinations:
      self.run(dest, string, nextIndex, historic + [dest])
      destinationsEpsilon = self.parser.transistions[(dest, 'epsilon')] if (dest, 'epsilon') in self.parser.transistions else []   
      for destEp in destinationsEpsilon:
        print(dest, destinationsEpsilon)
        self.run(destEp, string, nextIndex, historic + [dest, destEp])

    # destinationsEpsilon = self.parser.transistions[(actualState, 'epsilon')] if (actualState, 'epsilon') in self.parser.transistions else [] 
    # print(actualState, destinationsEpsilon)

    # for destEp in destinationsEpsilon:
    #   self.run(destEp, string, index, historic + [dest])