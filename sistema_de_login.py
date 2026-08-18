nome = input('Nome: ')
usuario = input('Usuario: ')
senha = input('Senha: ')
codigo = input('Codigo: ')

if (
    ('Arthur' in nome or 'Admin' in usuario)
     and ('A' in senha and '@' in senha) 
     and '123' not in senha and codigo == '5532'
     ):
    print(f"""==========================================
BEM VINDO DE VOLTA {nome}

Usuario: {nome}
Codigo: {codigo} 
==========================================""")