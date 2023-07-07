import random

def exibir_tabuleiro(tabuleiro):
    print("\n")
    print("\t " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("\t---+---+---")
    print("\t " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("\t---+---+---")
    print("\t " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])
    print("\n")

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for i in range(0, 7, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] == jogador:
            return True
    # Verificar colunas
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] == jogador:
            return True
    # Verificar diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == jogador:
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == jogador:
        return True
    return False

def jogar():
    tabuleiro = [' '] * 9
    jogadores = ['X', 'O']
    jogador_atual = random.choice(jogadores)
    jogo_em_andamento = True

    while jogo_em_andamento:
        exibir_tabuleiro(tabuleiro)
        print("Vez do jogador:", jogador_atual)
        posicao = input("Escolha uma posição (1-9): ")

        if not posicao.isdigit() or int(posicao) < 1 or int(posicao) > 9:
            print("Posição inválida! Tente novamente.")
            continue

        posicao = int(posicao) - 1

        if tabuleiro[posicao] == ' ':
            tabuleiro[posicao] = jogador_atual
        else:
            print("Posição ocupada! Tente novamente.")
            continue

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print("Jogador", jogador_atual, "venceu!")
            jogo_em_andamento = False
        elif ' ' not in tabuleiro:
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            jogo_em_andamento = False

        jogador_atual = jogadores[(jogadores.index(jogador_atual) + 1) % len(jogadores)]

    jogar_novamente = input("Deseja jogar novamente? (S/N): ")
    if jogar_novamente.upper() == 'S':
        jogar()

print("Bem-vindo ao Jogo da Velha!")
jogar()
