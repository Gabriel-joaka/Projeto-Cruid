# -*- coding: utf-8 -*-
"""proj computacionais.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OkFhyLxQwgYqM_DQEXPlduhdIpGkY3k1
"""

#bd = {usuario;user ,senha; password,compras;[obj, lugar, preco],saldo}
bd = {}
compra = []
rest = ['zuleika', 'papajohn', 'pipoqueiro', 'comida da vila']
comidas = ['pipoca','pipoca com manteiga','pipoca com queijo e bacon','pipoca doce','cafe coado','cafe expresso','cafe ao leite','cappucino','bolo','croassaint de chocolate','barra de chocolate','chiclete','salgados']
refri = ['coca-cola','coca-cola zero','guarana','energetico']
precos1 = [5,6.5,8,7,2,4,5,6,8,5,7,3,7.75]
precosR = [5,5,5,8]
def criar(usur, senha):
    bd['Usuario'] = usur
    bd['Senha'] = senha
    bd['Compras'] = []
    bd['Saldo'] = 0

def ver(usur, confsenha):
    if bd.get(senha) == confsenha:
        print('Usuário cadastrado.')
        return True
    else:
        print('As senhas não coincidem. Favor redigitar a senha.')
        return False

def botaohome(r):
  if r == 1:
        home = int(input('''
        1)pagina inicial
        2)perfil
        3)depositar
        4)configurações
        5)continuar
        '''))
        pag_ini(home)
def pag_ini(home):
        if home == 1:
            loja = int(input('''
            1)zuleika
            2)papajohn
            3)pipoqueiro
            4)comida da vila
            5)voltar
            '''))
            if loja != 5:
              compra.append(rest[loja-1])
              botaoloja(loja)
        elif home == 2:
          homeb = int(input(f'''
            1)exibir nome
            2)exibir senha
            3)exibir saldo
            4)voltar
            '''))
          if homeb == 1:
            print(bd['Usuario'])
          elif homeb == 2:
            print(bd['Senha'])
          elif homeb ==3:
            print(bd['Saldo'])
          elif homeb == 4:
            pag_ini(home)
        elif home == 3:
          deposito = int(input('''
            1)credito
            2)pix
            3)debito
            4)voltar
            '''))
          if deposito < 4:
            valor = float(input('Valor a depositar?'))
            bd['Saldo'] += valor
          else:
            pag_ini(home)
        elif home == 4:
          homebb = int(input(f'''
            1)mudar nome
            2)mudar senha
            3)mudar saldo
            4)voltar
            '''))
          if homebb == 1:
            nome = input('Qual será o novo nome:')
            bd['Usuario'] = nome
            print(bd['Usuario'], ' nome atualizado')
          elif homebb == 2:
            nome = input('Qual será a nova senha:')
            bd['Senha'] = nome
            print(bd['Usuario'], ' Senha atualizado')
          elif homebb ==3:
            nome = input('Qual será o novo Saldo:')
            bd['Saldo'] = nome
            print(bd['Saldo'], ' Saldo atualizado')
          elif homebb == 4:
            pag_ini(home)
        elif home == 5:
          ver = int(input('''
    Deseja continuar?
    1) Sim
    2) Não
    '''))
          if ver == 2:
            return False
def botaoloja(loja):
    if loja == 1 or loja == 2 or loja == 4:
        opc = int(input('''
        1) salgado
        2) doce
        3) cafe
        4) refrigerante
        5) voltar
        '''))
        if opc == 1:
            item = int(input('''
            1) coxinha
            2) kibe
            3) pao de queijo
            4) folhado
            5) voltar
            '''))
            if item == 5:
              botaoloja(loja)
            else:
              compra.append(comidas[(item+12)-1])
              compra.append(precos1[12])
        elif opc == 2:
            item = int(input('''
            1) bolo
            2) croassaint de chocolate
            3) barra de chocolate
            4) chiclete
            5) voltar
            ''' ))
            if item == 5:
              botaoloja(loja)
            else:
              compra.append(comidas[(item+8)-1])
              compra.append(precos1[(item+8)-1])
        elif opc == 3:
            item = int(input('''
            1) cafe coado
            2) cafe expresso
            3) barra ao leite
            4) cappuccino
            5) voltar
            ''' ))
            if item == 5:
              botaoloja(loja)
            else:
              compra.append(comidas[(item+4)-1])
              compra.append(precos1[(item+4)-1])
        elif opc == 4:
            item = int(input('''
            1) coca-cola
            2) coca-cola zero
            3) guarana
            4) energetico
            5) voltar
            ''' ))
            if item == 5:
              botaoloja(loja)
            else:
              compra.append(refri[item-1])
              compra.append(precosR[item-1])
        elif opc == 5:
          botaohome(r)
        else:
            print('Opção inválida')
    elif loja == 3:
      item = int(input('''
            1) pipoca
            2) pipoca com manteiga
            3) pipoca com queijo e bacon
            4) pipoca doce
            5)voltar
            ''' ))
      if item == 5:
        botaoloja(loja)
      else:
        compra.append(comidas[item-1])
        compra.append(precos1[item-1])
    elif loja == 5:
      botaohome(r)
    else:
        print('Opção inválida')

    ver = int(input('''
    Deseja confirmar a compra?
    1) Sim
    2) Não
    '''))
    if ver == 1:
      if float(compra[2]) <= bd['Saldo']:
        bd['Compras'] += compra
        bd['Saldo'] = float(bd['Saldo']) - float(compra[2])
        compra.clear()
      else:
        print('Saldo invalido ')
        compra.clear()
    else:
        compra.clear()

prog = True
while prog:
    usuario = input('Qual o nome do usuário? ')
    senha = input('Qual a senha? ')
    senha_conf = input('Confirme sua senha: ')
    if senha == senha_conf:
        criar(usuario, senha)
        r = 1
        while r == 1:
            botaohome(r)
            sair = int(input('Deseja sair?\n1) Sim\n2) Não\n'))
            if sair == 1:
                prog = False
                break
    else:
        r = 0
        print('As senhas não coincidem. Tente novamente.')

print(bd)