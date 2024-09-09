
reserved_words = [
    'class', 'def', 'if', 'else', 'return', 'True', 'False', 'None', 'while', 'for', 'print'
]

operators = {
    '+': 'tk_suma',
    '-': 'tk_resta',
    '*': 'tk_mult',
    '/': 'tk_div',
    '=': 'tk_asig',
    '(': 'tk_par_izq',
    ')': 'tk_par_der',
    ':': 'tk_dos_puntos',
    '.': 'tk_punto',
}

def is_digit(char):
    return '0' <= char <= '9'


def is_letter(char):
    return 'A' <= char <= 'Z' or 'a' <= char <= 'z' or char == '_'


def lexer(code):
    tokens = []
    i = 0
    line_num = 1
    column_num = 1

    while i < len(code):
        char = code[i]

        
        if char == '\n':
            line_num += 1
            column_num = 1
            i += 1
            continue

        
        if char.isspace():
            column_num += 1
            i += 1
            continue

        
        if char in operators:
            tokens.append(f'<{operators[char]},{line_num},{column_num}>')
            column_num += 1
            i += 1
            continue

        
        if is_digit(char):
            start_column = column_num
            number = char
            i += 1
            column_num += 1

            while i < len(code) and is_digit(code[i]):
                number += code[i]
                column_num += 1
                i += 1

            tokens.append(f'<tk_entero,{number},{line_num},{start_column}>')
            continue

        
        if is_letter(char):
            start_column = column_num
            identifier = char
            i += 1
            column_num += 1

            while i < len(code) and (is_letter(code[i]) or is_digit(code[i])):
                identifier += code[i]
                column_num += 1
                i += 1

            if identifier in reserved_words:
                tokens.append(f'<{identifier},{line_num},{start_column}>')
            else:
                tokens.append(f'<id,{identifier},{line_num},{start_column}>')
            continue

        break

    return tokens

with open('codigo_fuente.py', 'r') as file:
    code = file.read()

tokens = lexer(code)

# 6. Escribir la salida en un archivo
with open('output.txt', 'w') as output_file:
    for token in tokens:
        output_file.write(token + '\n')

print("Análisis léxico completado. Revisa el archivo output.txt para ver los resultados.")
