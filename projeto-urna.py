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




quantJoao = 0 
quantFernando = 0 
quantLarissa = 0
quantSouza = 0 
quantBranco = 0


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

    global quantJoao, quantFernando, quantLarissa, quantSouza, quantBranco
   
    escolha = True

    while escolha == True:
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
        esc = input("Deseja Votar novamente [S/N]: ").upper()
        if esc == 'N':
            escolha = False
            break
            
        

def exibirResultados():
    total_votos = quantBranco + quantFernando + quantJoao + quantLarissa + quantSouza
    total_votos_validos = quantFernando + quantJoao + quantLarissa + quantSouza

    print("======== RESULTADO DA ELEIÇÃO ========")
    print(f"Total de votos: {total_votos}")
    print(f"Total de votos válidos: {total_votos_validos}")
    print(f"Total de votos nulos/brancos: {quantBranco} - {quantBranco / total_votos * 100:.2f}%")

    print(f"\nJoâo Batista: {quantJoao} - {quantJoao / total_votos * 100:.2f}%")
    print(f"Fernando do Gás: {quantFernando} - {quantFernando / total_votos * 100:.2f}%")
    print(f"Larissa Gonçalves: {quantLarissa} - {quantLarissa / total_votos * 100:.2f}%")
    print(f"Souza da Água: {quantSouza} - {quantSouza / total_votos * 100:.2f}%")

    print("\n-- Percentuais sobre os votos válidos --")
    print(f"João Batista: {quantJoao / total_votos_validos * 100:.2f}%")
    print(f"Fernando do Gás: {quantFernando / total_votos_validos * 100:.2f}%")
    print(f"Larissa Gonçalves: {quantLarissa / total_votos_validos * 100:.2f}%")
    print(f"Souza da água: {quantSouza / total_votos_validos * 100:.2f}%")






loginUrnaVotacao(senha)
exibirResultados()



