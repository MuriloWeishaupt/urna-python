print("BEM VINDO A URNA ELEITORAL")

def criaSenha():
    global senha
    senha = input("Crie sua senha: ")
    senha2 = input("Confirme sua senha: ")
    while senha != senha2:
        print("Ambas senhas devem ser iguais! Tente novamente")
        senha = input("Crie sua senha: ")
        senha2 = input("Confirme sua senha: ")
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
    print("Voto em branco - Número do voto:    [0]")
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
        
        senhaLogin = input("Insira sua senha: ")
        while senha != senhaLogin:
            print("SENHA INVÁLIDA!")
            senhaLogin = input("Insira sua senha: ")
        
def segundoTurno(candidatos_empate):
    print("\n======== SEGUNDO TURNO ========")
    print("Candidatos empatados:")
    i = 1
    while i <= len(candidatos_empate):
        print(f"{i}.  {candidatos_empate[i - 1]}")
        i += 1

    votos_segundo_turno = []
    for i in range(len(candidatos_empate)):
        votos_segundo_turno.append(0)

    continuar = True
    while continuar:
        voto = int(input("Digite o número do candidato: "))
        if voto >= 1 and voto <= len(candidatos_empate):
            votos_segundo_turno[voto - 1] += 1
        else:
            print("Voto inválido!")

        esc = input("Deseja votar novamente no segundo turno [S/N]? ").upper()
        if esc == 'N':
            continuar = False

    print("\n======== RESULTADO DO SEGUNDO TURNO ========")
    i = 0
    while i < len(candidatos_empate):
        print(f"{candidatos_empate[i]}: {votos_segundo_turno[i]} votos")
        i += 1

    max_votos = max(votos_segundo_turno)
    vencedores = []
    i = 0
    while i < len(votos_segundo_turno):
        if votos_segundo_turno[i] == max_votos:
            vencedores.append(candidatos_empate[i])
        i += 1

    if len(vencedores) == 1:
        print("\n" + vencedores[0] + " é o(a) vencedor(a) do segundo turno!")
    else:
        print("\nEmpate novamente no segundo turno entre:")
        for nome in vencedores:
            print("- " + nome)

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

    print("\nCANDIDATO ELEITO:")

    if quantJoao > quantFernando and quantJoao > quantLarissa and quantJoao > quantSouza:
        print(f"João Batista é eleito com {quantJoao} votos!")

    elif quantFernando > quantJoao and quantFernando > quantLarissa and quantFernando > quantSouza:
        print(f"Fernando do Gás é eleito com {quantFernando} votos!")
    
    elif quantLarissa > quantJoao and quantLarissa > quantFernando and quantLarissa > quantSouza:
        print(f"Larissa Gonçalves é eleita com {quantLarissa} votos!")

    elif quantSouza > quantJoao and quantSouza > quantFernando and quantSouza > quantLarissa:
        print(f"Souza da água é eleito com {quantSouza} votos!")

    else:
        print("Houve um empate entre os candidatos!")
        print(f"João Batista: {quantJoao} votos")
        print(f"Fernando do Gás: {quantFernando} votos")
        print(f"Larissa Gonçalves: {quantLarissa} votos")
        print(f"Souza da água: {quantSouza} votos")

        candidatos_empate = []
        maior_voto = max(quantJoao, quantFernando, quantLarissa, quantSouza)

        if quantJoao == maior_voto:
            candidatos_empate.append("João Batista")
        if quantFernando == maior_voto:
            candidatos_empate.append("Fernando do Gás")
        if quantLarissa == maior_voto:
            candidatos_empate.append("Larissa Gonçalves")
        if quantSouza == maior_voto:
            candidatos_empate.append("Souza da água")

        segundoTurno(candidatos_empate)

loginUrnaVotacao(senha)
exibirResultados()
