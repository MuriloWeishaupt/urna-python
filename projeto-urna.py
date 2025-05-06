print("BEM VINDO A URNA ELEITORAL")

def criaSenha():
    global senha
    senha = input("Crie sua senha: ")
    senha2 = input("Confirme sua senha: ")
    while (senha != senha2):
        print("Ambas senhas devem ser iguais! Tente novamente")
        senha = input("Crie sua senha: ")
        senha2 = input("Confirme sua senha: ")
        if senha == senha2:
            break
    print("-----------------------------")
    print("Senha cadastrada com sucesso!")
    

criaSenha()


def loginUrnaVotacao(senha):
    senhaLogin = input("Insira sua senha: ")
    while senha != senhaLogin:
        print("SENHA INVÁLIDA!")
        senhaLogin = input("Insira sua senha: ")
    print("-----------------------------")
    print("Login Concluído")

    print("======== CANDIDATOS ELEIÇÃO ========")
    print()
    print("João Batista - Número do voto:      [19]")
    print("Fernando do Gás - Número do voto:   [10]")
    print("Larissa Gonçalves - Número do voto: [16]")
    print("Souza da água - Número do voto:     [12]")

    votoJoao = 19
    votoFernando = 10
    votoLarissa = 16
    votoSouza = 12
    votoBranco = 0

    quantJoao, quantFernando, quantLarissa, quantSouza, quantBranco = 0

    escolha = True

    voto = int(input("Digite o seu voto: "))

    if voto == votoJoao:
        quantJoao += 1
    elif voto == votoFernando:
        quantFernando += 1
    elif voto == votoLarissa:
        quantLarissa += 1
    elif voto == votoSouza:
        quantSouza += 1
    elif voto == votoBranco:
        quantBranco += 1
    else:
        quantBranco += 1


    while escolha == True:
        esc = input("Deseja Votar novamente [S/N]: ").upper()
        if esc == 'S':
            escolha == False
            break
        
        

loginUrnaVotacao(senha)



