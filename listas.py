def menu():
  while True:
    print('### APC ###')
    print()
    print('Opcoes:')
    print('1 - Cadastrar aluno')
    print('2 - Entrada e notas')
    print('3 - Ver Extrato geral')
    op = int(input('digite o numero da opcao desejada: '))
    if 1 <= op <=3:
      return op



def efetua_cadastro(cadastro):
  nome = input('Digite o seu nome: ')
  sobrenome = input('Digite seu sobrenome: ')
  matricula = input('Digite sua matricula: ')
  notas_le = [0.0] * 11
  notas_p = [0.0] * 3
  cadastro.append([nome, sobrenome, matricula, notas_le, notas_p])


def entrada_notas(cadastro):
  if len(cadastro) == 0:
    print('Você precisa cadastrar um aluno primeiro!')
  else:
    mat = input('Buscar pela matricula: ')
    achou = False
    for i in range(len(cadastro)):
      if cadastro[i][2] == mat:
        achou = True
        print(f'Entre com as notas de {cadastro[i][0]} {cadastro[i][1]}: ')
        for l in range(len(cadastro[i][3])):
          cadastro[i][3][l] = float(input(f'Lista {l+1} ({cadastro[i][3][l]:.1f}): '))
        
        for p in range(len(cadastro[i][4])):
          cadastro[i][4][p] = float(input(f'Projeto {p+1} ({cadastro[i][4][p]:.1f}): '))
        break 
    if not achou:
      print(f'A Matricula {mat} não foi encontrada')

      

def calcula_media_lista(lista):
  return sum(lista)/len(lista)

def calcula_nota_final_apc(le, p):
  if le >=5 and p>=5:
    nf =  (0.4*le) + (0.6 * p)
  
  else:
    nf = 0.0
    
  return nf

def extrato(cadastro):
  for i in range(len(cadastro)):
    linha = '#' * (len(cadastro[i][0]) + len(cadastro[i][1])+ len(cadastro[i][2]) + 8)
    print(linha)
    print(f'#{cadastro[i][0]} {cadastro[i][1]} ({cadastro[i][2]})#')
    print(linha)

    for l in range(len(cadastro[i][3])):
      print(f'Lista {l+1} \t({cadastro[i][3][l]:.1f})')
    for p in range(len(cadastro[i][4])):
       print(f'Projeto {p+1} \t({cadastro[i][4][p]:.1f})')
    
    media_le = calcula_media_lista(cadastro[i][3])
    media_p = calcula_media_lista(cadastro[i][4])
    n_final = calcula_nota_final_apc(media_le,media_p)
    print(f'LE = {media_le:.1f}')
    print(f'P = {media_p:.1f}')
    print(f'NF = {n_final:.1f}')







cadastro = []

continua = 's'
while continua != 'n':
  op = menu()

  if op ==1:
    efetua_cadastro(cadastro)
  
  elif op==2:
    entrada_notas(cadastro)
  
  elif op ==3:
    extrato(cadastro)
  
  continua = input('deseja continuar? (s/n) ')