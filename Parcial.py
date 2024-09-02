# Definición de las palabras reservadas y símbolos
reserved_words = [
    'class', 'def', 'if', 'else', 'return', 'True', 'False', 'None', 'while', 'for', 'print',
    '__init__', 'in', 'not', 'and', 'or', 'is', 'from', 'import', 'as', 'pass', 'break', 'continue',
    'elif', 'with', 'lambda', 'try', 'except', 'finally', 'raise', 'yield', 'global', 'nonlocal',
    'assert', 'del'
]

# Definición de operadores y símbolos, incluyendo operadores de múltiples caracteres
operators = {
    '==': 'tk_igual',
    '!=': 'tk_distinto',
    '<=': 'tk_menor_igual',
    '>=': 'tk_mayor_igual',
    '->': 'tk_ejecuta',
    '+': 'tk_suma',
    '-': 'tk_resta',
    '*': 'tk_mult',
    '/': 'tk_div',
    '%': 'tk_modulo',
    '=': 'tk_asig',
    '<': 'tk_menor',
    '>': 'tk_mayor',
    ':': 'tk_dos_puntos',
    '(': 'tk_par_izq',
    ')': 'tk_par_der',
    '[': 'tk_corchete_izq',
    ']': 'tk_corchete_der',
    '{': 'tk_llave_izq',
    '}': 'tk_llave_der',
    ',': 'tk_coma',
    '.': 'tk_punto',
    ';': 'tk_punto_y_coma',
}

# Ordenamos los operadores por longitud decreciente para maximal munch
operators_keys = sorted(operators.keys(), key=lambda x: -len(x))

# Función para verificar si un carácter es un dígito
def is_digit(char):
    return '0' <= char <= '9'

# Función para verificar si un carácter es una letra o subrayado
def is_letter(char):
    return ('A' <= char <= 'Z') or ('a' <= char <= 'z') or char == '_'

# Función principal del analizador léxico
def lexer(code):
    tokens = []
    i = 0
    line_num = 1
    column_num = 1
    length = len(code)
    
    while i < length:
        char = code[i]
        
        # Saltos de línea
        if char == '\n':
            line_num += 1
            column_num = 1
            i += 1
            continue
        
        # Espacios en blanco y tabulaciones
        if char == ' ' or char == '\t' or char == '\r':
            column_num += 1
            i += 1
            continue
        
        # Ignorar comentarios
        if char == '#':
            while i < length and code[i] != '\n':
                i += 1
                column_num += 1
            continue
        
        # Manejo de cadenas de texto
        if char == '"' or char == "'":
            start_line = line_num
            start_column = column_num
            quote_type = char
            string_literal = char
            i += 1
            column_num += 1
            while i < length:
                current_char = code[i]
                string_literal += current_char
                if current_char == '\\':  # Carácter de escape
                    i += 1
                    column_num += 1
                    if i < length:
                        string_literal += code[i]
                        i += 1
                        column_num += 1
                    else:
                        # Error: cadena no terminada
                        tokens.append(f'>>> Error lexico(linea:{line_num},posicion:{column_num})')
                        return tokens
                    continue
                elif current_char == quote_type:
                    i += 1
                    column_num += 1
                    tokens.append(f'<tk_cadena,{string_literal},{start_line},{start_column}>')
                    break
                elif current_char == '\n':
                    # Error: cadena no terminada en la misma línea
                    tokens.append(f'>>> Error lexico(linea:{line_num},posicion:{start_column})')
                    return tokens
                else:
                    i += 1
                    column_num += 1
            else:
                # Error: cadena no cerrada
                tokens.append(f'>>> Error lexico(linea:{start_line},posicion:{start_column})')
                return tokens
            continue
        
        # Operadores y símbolos
        matched = False
        for op in operators_keys:
            op_len = len(op)
            if code[i:i+op_len] == op:
                tokens.append(f'<{operators[op]},{line_num},{column_num}>')
                i += op_len
                column_num += op_len
                matched = True
                break
        if matched:
            continue
        
        # Números (enteros y flotantes)
        if is_digit(char):
            start_column = column_num
            number = ''
            has_decimal_point = False
            while i < length and (is_digit(code[i]) or code[i] == '.'):
                if code[i] == '.':
                    if has_decimal_point:
                        # Error: más de un punto decimal
                        tokens.append(f'>>> Error lexico(linea:{line_num},posicion:{column_num})')
                        return tokens
                    has_decimal_point = True
                number += code[i]
                i += 1
                column_num += 1
            # Verificamos que el número no termine con un punto
            if number.endswith('.'):
                # Error: número no puede terminar con punto decimal
                tokens.append(f'>>> Error lexico(linea:{line_num},posicion:{column_num - 1})')
                return tokens
            if has_decimal_point:
                tokens.append(f'<tk_flotante,{number},{line_num},{start_column}>')
            else:
                tokens.append(f'<tk_entero,{number},{line_num},{start_column}>')
            continue
        
        # Identificadores y palabras reservadas
        if is_letter(char):
            start_column = column_num
            identifier = ''
            while i < length and (is_letter(code[i]) or is_digit(code[i])):
                identifier += code[i]
                i += 1
                column_num += 1
            if identifier in reserved_words:
                tokens.append(f'<{identifier},{line_num},{start_column}>')
            else:
                tokens.append(f'<id,{identifier},{line_num},{start_column}>')
            continue
        
        # Error léxico genérico
        tokens.append(f'>>> Error lexico(linea:{line_num},posicion:{column_num})')
        return tokens

    return tokens

# Función principal para leer el archivo de entrada y escribir la salida
def main():
    input_filename = 'codigo_fuente.py'  # Nombre del archivo de entrada
    output_filename = 'output.txt'       # Nombre del archivo de salida
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            code = file.read()
    except FileNotFoundError:
        print(f'Error: El archivo {input_filename} no existe.')
        return
    tokens = lexer(code)
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for token in tokens:
            output_file.write(token + '\n')
    print(f'Análisis léxico completado. Revisa el archivo {output_filename} para ver los resultados.')

if __name__ == '__main__':
    main()
