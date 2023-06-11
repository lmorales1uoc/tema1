def fibonacci(fibonacci_number):
    #Antes que nada, hay que entender cómo funciona esta secuencia. Menos para 0 y 1, partimos de la base que n = n-1 + n-2
    if fibonacci_number < 0 or isinstance(fibonacci_number, float): #condición valor inválido si es menor a 0 o es un valor decimal
        raise ValueError("A number lower than 0 or decimal numbers are not allowed") #lanzamos el error si no se cumplen las condiciones
    if fibonacci_number < 2: #La fórmula matemática para la secuencia aplica a partir del número 2. Los números 1 y 2 devuelven su misma posición
        return fibonacci_number
    else: #v. comentario de la línea 3, es la fórmula aplicada
        return fibonacci (fibonacci_number-1) + fibonacci(fibonacci_number-2)

print(fibonacci(-10))

## Bibliografía: https://pythondiario.com/2018/08/sucesion-de-fibonacci-con-python.html
