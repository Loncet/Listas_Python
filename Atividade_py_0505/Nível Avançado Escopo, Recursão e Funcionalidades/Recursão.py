def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        return fibonacci(n - 1) + fibonacci(n - 2)

termo = 6
resultado = fibonacci(termo)
print(f"O {termo}º termo da sequência de Fibonacci é: {resultado}")