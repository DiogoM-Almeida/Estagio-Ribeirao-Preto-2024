def reverse_string(input_string):
    reversed_string = ""
    index = 0
    while input_string[index:]:
        index += 1
    index -= 1
    while index >= 0:
        reversed_string += input_string[index]
        index -= 1
    return reversed_string

original_text = input("Digite uma string para inverter: ")
reversed_text = reverse_string(original_text)
print("String original:", original_text)
print("String invertida:", reversed_text)