
from datetime import date
T = int(input())
n = int(input())
i = 0
regular = 0
irregular = 0
masc = 0
fem = 0
media_ingresso = 0
ano_atual = 2019
data = 0
indice_semana = 0
domingo = 0
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0
sabado = 0
domingoF = 0
segundaF = 0
tercaF = 0
quartaF = 0
quintaF = 0
sextaF = 0
sabadoF = 0
regularM = 0
regularF = 0
irregularM = 0
irregularF = 0
totalRegularM = 0
totalIrregularM = 0
totalRegularF = 0
totalIrregularF = 0
media_regulares = 0
media_irregulares = 0
media_ingresso = 0
media_ingressoF = 0
tempo_total = 0
tempo_totalF = 0
contaM = 0
contaF = 0

while i < n:
    try:

        NU_ANO_INGRESSO, NU_DIA_NASCIMENTO, NU_MES_NASCIMENTO, NU_ANO_NASCIMENTO, TP_SEXO, TP_SITUACAO = input().split()
        NU_ANO_INGRESSO = int(NU_ANO_INGRESSO)
        NU_DIA_NASCIMENTO = int(NU_DIA_NASCIMENTO)
        NU_MES_NASCIMENTO = int(NU_MES_NASCIMENTO)
        NU_ANO_NASCIMENTO = int(NU_ANO_NASCIMENTO)
        TP_SEXO = int(TP_SEXO)
        TP_SITUACAO = int(TP_SITUACAO)

        if T == 1:
            if TP_SITUACAO == 2 or TP_SITUACAO == 6:
                regular = regular + 1
            else:
                irregular = irregular + 1

            if i == n-1:
                print(f'matriculados ou formados: {(regular*10):.1f}')
                print(f'alunos em outras situacoes: {(irregular*10):.1f}')

        elif T == 2:
            if TP_SEXO == 1:
                fem = fem + 1
            else:
                masc = masc + 1

            if i == n-1:
                print(f"sexo masculino: {(masc*100)/n:.1f}")
                print(f"sexo feminino: {(fem*100)/n:.1f}")

        elif T == 3:
            anos = NU_ANO_INGRESSO
            tempo_de_curso = ano_atual - anos
            tempo_total = tempo_de_curso/n
            media_ingresso = media_ingresso + tempo_total

            if i == n-1:
                print(f'media de anos desde ingresso:%5.1f' % (media_ingresso))

        elif T == 4:

            data = date(year=NU_ANO_NASCIMENTO,
                        month=NU_MES_NASCIMENTO, day=NU_DIA_NASCIMENTO)
            indice_semana = data.isoweekday()
            if indice_semana == 1:
                segunda = segunda + 1
            elif indice_semana == 2:
                terca = terca + 1

            elif indice_semana == 3:
                quarta = quarta + 1

            elif indice_semana == 4:
                quinta = quinta + 1

            elif indice_semana == 5:
                sexta = sexta + 1

            elif indice_semana == 6:
                sabado == sabado+1

            elif indice_semana == 7:
                domingo = domingo+1

            if i == n-1:
                print(f'domingo:%5.1f' % (domingo*10))
                print(f'segunda:%5.1f' % (segunda*10))
                print(f'terca:%5.1f' % (terca*10))
                print(f'quarta:%5.1f' % (quarta*10))
                print(f'quinta:%5.1f' % (quinta*10))
                print(f'sexta:%5.1f' % (sexta*10))
                print(f'sabado:%5.1f' % (sabado*10))

        elif T == 5:
            if (TP_SITUACAO == 2 or TP_SITUACAO == 6) and TP_SEXO == 2:
                regularM = regularM + 1
                masc = masc + 1

            elif (TP_SITUACAO != 2 or TP_SITUACAO != 6) and TP_SEXO == 2:
                irregularM = irregularM + 1
                masc = masc + 1

            if (TP_SITUACAO == 2 or TP_SITUACAO == 6) and TP_SEXO == 1:
                regularF = regularF + 1
                fem = fem + 1
            elif (TP_SITUACAO != 2 or TP_SITUACAO != 6) and TP_SEXO == 1:
                irregularF = irregularF + 1
                fem = fem + 1
            if i == n-1:
                print('dentre masculinos:')
                print(f'matriculados ou formados:%5.1f' %
                      ((regularM*100)/masc))
                print(f'alunos em outras situacoes:%5.1f' %
                      ((irregularM*100)/masc))
                print('dentre femininos:')
                print(f'matriculados ou formados:%5.1f' % ((regularF*100)/fem))
                print(f'alunos em outras situacoes:%5.1f' %
                      ((irregularF*100)/fem))

        elif T == 6:
            if TP_SITUACAO == 2 or TP_SITUACAO == 6:
                anos = NU_ANO_INGRESSO
                tempo_de_curso = ano_atual - anos
                tempo_total = tempo_de_curso + tempo_total
                media_regulares = media_regulares + 1

            else:
                anos = NU_ANO_INGRESSO
                tempo_de_curso = ano_atual - anos
                tempo_totalF = tempo_de_curso + tempo_totalF
                media_irregulares = media_irregulares + 1

            if i == n-1:

                print('dentre matriculados ou formados:')
                print(f'media de anos desde ingresso:%5.1f' %
                      (tempo_total/media_regulares))
                print('dentre alunos em outras situacoes:')
                print(f'media de anos desde ingresso:%5.1f' %
                      (tempo_totalF/media_irregulares))

        elif T == 7:
            if TP_SEXO == 2:
                contaM = contaM + 1
                data = date(year=NU_ANO_NASCIMENTO,
                            month=NU_MES_NASCIMENTO, day=NU_DIA_NASCIMENTO)
                indice_semana = data.isoweekday()
                if indice_semana == 1:
                    segunda = segunda + 1
                elif indice_semana == 2:
                    terca = terca + 1

                elif indice_semana == 3:
                    quarta = quarta + 1

                elif indice_semana == 4:
                    quinta = quinta + 1

                elif indice_semana == 5:
                    sexta = sexta + 1

                elif indice_semana == 6:
                    sabado = sabado+1

                elif indice_semana == 7:
                    domingo = domingo+1

            else:
                contaF = contaF+1
                data = date(year=NU_ANO_NASCIMENTO,
                            month=NU_MES_NASCIMENTO, day=NU_DIA_NASCIMENTO)
                indice_semana = data.isoweekday()
                if indice_semana == 1:
                    segundaF = segundaF + 1
                elif indice_semana == 2:
                    tercaF = tercaF + 1

                elif indice_semana == 3:
                    quartaF = quartaF + 1

                elif indice_semana == 4:
                    quintaF = quintaF + 1

                elif indice_semana == 5:
                    sextaF = sextaF + 1

                elif indice_semana == 6:
                    sabadoF = sabadoF+1

                elif indice_semana == 7:
                    domingoF = domingoF+1

            if i == n-1:
                print("dentre masculinos:")
                print(f'domingo:%5.1f' % (domingo*100/contaM))
                print(f'segunda:%5.1f' % (segunda*100/contaM))
                print(f'terca:%5.1f' % (terca*100/contaM))
                print(f'quarta:%5.1f' % (quarta*100/contaM))
                print(f'quinta:%5.1f' % (quinta*100/contaM))
                print(f'sexta:%5.1f' % (sexta*100/contaM))
                print(f'sabado:%5.1f' % (sabado*100/contaM))
                print("dentre femininos:")
                print(f'domingo:%5.1f' % (domingoF*100/contaF))
                print(f'segunda:%5.1f' % (segundaF*100/contaF))
                print(f'terca:%5.1f' % (tercaF*100/contaF))
                print(f'quarta:%5.1f' % (quartaF*100/contaF))
                print(f'quinta:%5.1f' % (quintaF*100/contaF))
                print(f'sexta:%5.1f' % (sextaF*100/contaF))
                print(f'sabado:%5.1f' % (sabadoF*100/contaF))

        i = i + 1

    except EOFError:
        break
