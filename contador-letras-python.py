frase = 'O Python é uma linguagem de programação '\
'multiparadgma, '\
'Python foi criado por Guido Van Rossum.'.lower()
i = 0
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
maior_quantidade = 0
letra_mais_frequente = ''
while i < 26:
    i2 = abc[i]
    letra = frase.count(i2)
    if letra >= maior_quantidade:
        maior_quantidade = letra
        letra_mais_frequente = i2
    print(f'A letra {i2.upper()} apareceu {letra} vezes')
    i += 1
print(f'A letra que mais aparece em "{frase.capitalize()}" é {letra_mais_frequente.upper()}, que apareceu {maior_quantidade}x')