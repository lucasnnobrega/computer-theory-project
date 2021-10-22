class MultipleInputs:

  def __init__(self, inputfile):
    self.string_input = []
    self.read(inputfile)
    
  def read(self, inputfile):
    with open(inputfile, "r") as file:
      for line in file.readlines():
        self.string_input.append(line.rstrip('\n'))
          
        
  def show(self):
    print("Strings Input:")
    print(*self.string_input, sep="\n")

  def get_inputs(self):
    return self.string_input
    