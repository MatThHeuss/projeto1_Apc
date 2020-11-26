import os
import pickle
#Constantes globais
NUM_LISTAS = 11
NUM_PROJETOS = 3

#Funções
def menu():
  opcoes = {
    '1':'Cadastra aluno',
    '2':'Entrada de notas',
    '3':'Dados aluno',
    '4':'Ver extrato geral',
    '5':'Exportar dados dos alunos'
  }
  while True:
    print("\n#### APC ####\nOpcoes: ")
    for opcao,descricao in sorted(opcoes.items()):
      print(f'{opcao} - {descricao}')
    opcao = input("\nDigite o numero da opcao desejada: ")

    if opcao in opcoes:
      return opcao


def efetua_cadastro(cadastro):
  matricula = input("Digite sua matricula na Unb: ")
  registra = True
  if matricula in cadastro:
    registro = cadastro[matricula]
    if input(f'{registro["nome"]} ja esta cadastrado.\n'
    'Voce deseja sobrescrever o registro (s/n?)') == 'n':
      registra = False;
  if registra:
    cadastro[matricula] = {'nome':input("Digite seu nome completo: "),
    'listas':[0.0]*NUM_LISTAS,
    'projetos':[0.0]*NUM_PROJETOS}


def entrada_notas(cadastro):
  if cadastro:
    matricula = input('Buscar pela matricula: ')
    if matricula in cadastro:
      registro = cadastro[matricula]
      print(f'Entre com as notas de {registro["nome"]}:')
      registro['listas'] = [float(input(f'lista {nota_le + 1}: '))
      for nota_le in range(NUM_LISTAS)]

      registro['projetos'] = [float(input(f'Projeto {nota_p + 1}: '))
      for nota_p in range(NUM_PROJETOS)]
    
    else:
      print(f'A matricula {matricula} não foi encontrada')
  else:
    print("Voce precisa cadastrar um aluno primeiro!")


def registro(cadastro):
  if cadastro:
    matricula = input('Buscar pela matricula: ')
    if matricula in cadastro:
      imprime_registro(matricula, cadastro[matricula])
    else:
      print(f'A matricula {matricula} não foi encontrada')
  else:
    print('Voce precisa cadastrar um aluno primeiro!')



def imprime_registro(matricula, registro):
  aluno = (f"{matricula} - {registro['nome']}")
  print('#' * (len(aluno) + 4))
  print(f"# {aluno} #")
  print('#' * (len(aluno) + 4))

  for i, nota_le in enumerate(registro['listas']):
    print(f'Lista {i + 1}\t({nota_le:.1f})')
  
  for i, nota_p in enumerate(registro['projetos']):
    print(f'Projetos {i + nota_p}\t({nota_p:.1f})')




def media(lista):
  return sum(lista)/len(lista)

def nota_final(nota_le, nota_p):

  nota_final = (0.4 * nota_le) + (0.6 * nota_p)
  if nota_le < 5.0 or nota_p < 5.0:
    nota_final = min(nota_final, 4.9)
  
  return nota_final


def extrato(cadastro):
  for matricula in cadastro:
    registro = cadastro[matricula]
    imprime_registro(matricula,registro)

    media_le = media(registro['listas'])
    media_p = media(registro['projetos'])
    n_final = nota_final(media_le, media_p)
    print(f'LE = {media_le:.1f}')
    print(f'P = {media_p:.1f}')
    print(f'NF = {n_final:.1f}')
  
def exporta_alunos(cadastro, nome_arq):
  if os.path.exists(nome_arq)\
   and input('voce deseja sobrescrever o arquivo? (s/n)') in 'Ss'\
   or not os.path.exists(nome_arq):
   with open(nome_arq, 'w') as arq:
     for matricula, registro in cadastro.items():
       notas_le = ';'.join(map(str,registro["listas"])) 
       notas_p = ';'.join(map(str,registro["projetos"])) 
       arq.write(f'{matricula};{registro["nome"]};{notas_le};{notas_p}\n')





# Inicio do programa
nome = 'cadastro.bin'
cadastro = {}

# Carrega o cadastro
if os.path.isfile(nome):
  with open(nome, 'rb') as arquivo:
    cadastro = pickle.load(arquivo)

continua = 's'
while continua != 'n':
  op = menu()

  if op == '1':
    efetua_cadastro(cadastro)
  
  elif op == '2':
    entrada_notas(cadastro)

  elif op =='3':
    registro(cadastro)

  elif op == '4':
    extrato(cadastro)

  elif op =='5':
    nome_arq = input("Digite o nome do arquivo: ")
    exporta_alunos(cadastro,nome_arq)
  
  continua = input("Deseja continuar? (s/n)")


#Salva o cadastro
with open(nome, 'wb') as arquivo:
  pickle.dump(cadastro, arquivo)