matricula = input('Ola, voce esta matriculado na escola, PYTHON GUIDE? [S] [N] ')
ras = ['552','1111','0012']
alunos = ['Arthur','Lucas','Jennifer']
if matricula == 'S':
    nome = input('Qual o seu nome? ')
    ra = input('Qual o seu registro de aluno?(RA): ')
    if nome in alunos and ra in ras:
        nota_mat = float(input('Qual sua nota de matematica? '))
        nota_por = float(input('Qual sua nota de portugues? '))
        nota_py = float(input('Qual sua nota de python? '))
        print('Calculando...')
        media = (nota_mat + nota_por + nota_py) / 3
        print(f"""==================================
        {'Boletim':^16}
==================================
Aluno: {nome}
Matematica: {nota_mat:>7.2f}
Portugues:  {nota_por:>7.2f}
Python:     {nota_py:>7.2f}
Media:      {media:>7.2f}
==================================""")
    else:
        print('Voce nao esta na lista de alunos, tente novamente')
elif matricula == 'N':
    print('Okay, tenha um bom dia')
elif not matricula:
    print('Digite corretamente')
else:
    print('Digite apenas S ou N.')

