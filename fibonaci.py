# Secuencia de Fibonacci de forma iterativa
def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

# Secuencia de Fibonacci de forma recursiva
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Llamar a ambas funciones
def main():
    n = 10
    print(fibonacci_iterative(n))
    print(fibonacci_recursive(n))

if __name__ == "__main__":
    main()