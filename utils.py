def checkStringToAlphabet(alphabet, string):
  for element in string:
    if element not in alphabet:
      return False