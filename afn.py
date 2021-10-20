class AFN:

  def __init__(self, parser):
    self.parser = parser
    self.logs = []
    self.errors = []
    self.accepted = False
    pass

  def run(self, actualState, string, index):

    print("Actual state: {}".format(actualState))

    print(len(string) == index and actualState in self.parser.finals)

    if (len(string) == index and actualState in self.parser.finals):
      self.accepted = True
      return

    print(actualState, " -> ", string[index])

    char = string[index] if string[index] != ' ' else 'epsilon'

    destinations = self.parser.transistions[(actualState, char)]
    print("Possible destinitations: {}".format(destinations))

    if (len(destinations) == 0):
      self.errors.append(string[0:index+1])
      return

    for dest in destinations:
      self.run(dest, string, index + 1)