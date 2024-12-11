# calcula o n-ésimo número de Fibonacci
def fibonacci(n):
    # se fibonacci de 0 ou 1 é ele mesmo
    if n <= 1:
        return n  
    # soma dos dois números anteriores
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
n = 10
resultado = fibonacci(n)
print(f"O {n}-ésimo número de Fibonacci é: {resultado}")
