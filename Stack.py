class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items)-1]
  def size(self):
    return len(self.items)




def decimalToBinary(decNumber):
  s = Stack()

  while decNumber > 0:
    rem = decNumber % 2
    s.push(rem)

    decNumber = decNumber // 2
  
  binString = ''

  while not s.isEmpty():
    binString = binString + str(s.pop())
  
  return binString



resultado = decimalToBinary(233)

print(resultado)