def fibonacci_sequence(n):
    fibonacci_list = [0, 1]
    while fibonacci_list[-1] < n:
        next_value = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_value)
    return fibonacci_list

def check_fibonacci_number(number):
    fibonacci_list = fibonacci_sequence(number)
    if number in fibonacci_list:
        return f"{number} pertence à sequência de Fibonacci."
    else:
        return f"{number} não pertence à sequência de Fibonacci."

if __name__ == "__main__":
    num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    print(check_fibonacci_number(num))
