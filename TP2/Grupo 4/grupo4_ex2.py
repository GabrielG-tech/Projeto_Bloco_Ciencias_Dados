# calcula o fatorial de um num
def fatorial(n):
    # fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:  
        return 1
    # n * fatorial(n-1)
    else:
        return n * fatorial(n - 1)
numero = 5
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
