def torres_hanoi(n, origem, destino, auxiliar):
    # move o único disco de origem para destino
    if n == 1:  
        print(f"Move disco 1 de {origem} para {destino}")
        return
    # move n-1 discos da origem para a torre auxiliar
    torres_hanoi(n - 1, origem, auxiliar, destino)
    # move o disco maior da origem para o destino
    print(f"Move disco {n} de {origem} para {destino}")
    # move os n-1 discos da torre auxiliar para o destino
    torres_hanoi(n - 1, auxiliar, destino, origem)

numero_discos = 3  #
# A: origem, C: destino, B: auxiliar
torres_hanoi(numero_discos, 'A', 'C', 'B')  
