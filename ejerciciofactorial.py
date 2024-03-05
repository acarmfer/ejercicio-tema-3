#generame una funcion interactiva del facotrial de 5 
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = 5
print(factorial(n))

#generame una funcion recursiva del facotrial de 5 
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

print(recursive_factorial(5))

# Llamar a ambas funciones
def main():
    n = 5
    print(factorial(n))
    print(recursive_factorial(n))

if __name__ == "__main__":
    main()
    
  

    
    