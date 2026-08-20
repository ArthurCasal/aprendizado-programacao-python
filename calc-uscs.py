afs = int(input("Quantas AF's voce teve? [0 a 4] "))
n1 = float(input('Qual sua nota na N1? '))
ai = float(input('Qual sua nota na A1? '))

if afs == 1:
    nota_af1 = float(input('Qual foi sua nota da AF 1 '))
    media = (n1 + ((ai + nota_af1) / 2)) / 2
    print(f"""===============================
    {'Boletim':^20}

Notas AF:    {nota_af1:.2f}
Nota N1:     {n1:.2f}
Nota AI:     {ai:.2f}
Media N2:    {(ai + nota_af1)/2:.2f}
Media final: {media:.2f}
===============================  """)
elif afs == 2:
    nota_af1 = float(input('Qual foi sua nota da AF 1 '))
    nota_af2 = float(input('Qual foi sua nota da AF 2 '))
    media = (n1 + ((ai + ((nota_af1 + nota_af2)/2)) / 2)) / 2
    print(f"""===============================
    {'Boletim':^20}

Notas AF:    {(nota_af1 + nota_af2) / 2:.2f}
Nota N1:     {n1:.2f}
Nota AI:     {ai:.2f}
Media N2:    {(ai + ((nota_af1 + nota_af2)/ 2))/2:.2f}
Media final: {media:.2f}
===============================  """)
elif afs == 3:
    nota_af1 = float(input('Qual foi sua nota da AF 1 '))
    nota_af2 = float(input('Qual foi sua nota da AF 2 '))
    nota_af3 = float(input('Qual foi sua nota da AF 3 '))
    media = (n1 + ((ai + ((nota_af1 + nota_af2 + nota_af3)/3)) / 2)) / 2
    print(f"""===============================
    {'Boletim':^20}
    
Notas AF:    {(nota_af1 + nota_af2 + nota_af3) / 3:.2f}
Nota N1:     {n1:.2f}
Nota AI:     {ai:.2f}
Media N2:    {(ai + ((nota_af1 + nota_af2 + nota_af3)/ 3))/2:.2f}
Media final: {media:.2f}
===============================  """)
elif afs == 4:
    nota_af1 = float(input('Qual foi sua nota da AF 1 '))
    nota_af2 = float(input('Qual foi sua nota da AF 2 '))
    nota_af3 = float(input('Qual foi sua nota da AF 3 '))
    nota_af4 = float(input('Qual foi sua nota da AF 4 '))
    media = (n1 + ((ai + ((nota_af1 + nota_af2 + nota_af3 + nota_af4)/4)) / 2)) / 2
    print(f"""===============================
    {'Boletim':^20}
    
Notas AF:    {(nota_af1 + nota_af2 + nota_af3 + nota_af4) / 4:.2f}
Nota N1:     {n1:.2f}
Nota AI:     {ai:.2f}
Media N2:    {(ai + ((nota_af1 + nota_af2 + nota_af3 + nota_af4) / 4))/2:.2f}
Media final: {media:.2f}
===============================  """)
elif afs == 0:
    media = (n1 + ai) / 2
    print(f"""===============================
    {'Boletim':^20}
        
Nota N1:     {n1:.2f}
Nota AI:     {ai:.2f}
Media final: {media:.2f}
===============================  """)
elif afs > 4:
    print('Voce digitou uma AF a mais, tente novamente')

else:
    print('Voce nao digitou corretamente as AFS')

