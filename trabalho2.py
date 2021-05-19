class Stack:
  def __init__(self):
    self.items = []
    self.peso = 0
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

lista = []
lista_sobra = []
numero_wookies = int(input())

for i in range(0, numero_wookies):
  wookie = Stack()
  lista.append(wookie)


numero_cargas = input().split(" ")

for i in range(0, len(numero_cargas)):
  if i < numero_wookies:
     lista[i].push(int(numero_cargas[i]))
     lista[i].peso += int(numero_cargas[i])
     continue
  flag = False
  for j in range(0, len(lista)):
    if lista[j].peek() >= int(numero_cargas[i]):
      lista[j].push(int(numero_cargas[i]))
      lista[j].peso += int(numero_cargas[i])
      flag = True
      break
  
  if flag == False:
    lista_sobra.append(int(numero_cargas[i]))

     
lista_ordenada = sorted(lista, key= lambda x: x.peso, reverse=True)

if lista_ordenada == []:
  print("Os Wookies foram para o lado sombrio da força!")
else:
  for i in range(0, len(lista_ordenada)):
    print(lista_ordenada[i].items, end=" ")
  print()

if lista_sobra == []:
  print('A força está com os Wookies!')



for i in range(0, len(lista_sobra)):
 print(lista_sobra[i], end=" ")
