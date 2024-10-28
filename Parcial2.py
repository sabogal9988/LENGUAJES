import os
from Parcial import lexer  # Assuming lexer function is in Parcial.py

class AnalizadorSintactico:
    def __init__(self, entrada_path, salida_path):
        self.entrada_path = entrada_path
        self.salida_path = salida_path
        self.error = None

    def leer_archivo(self):
        try:
            with open(self.entrada_path, 'r', encoding='utf-8') as archivo:
                return archivo.read()
        except FileNotFoundError:
            self.error = f'Error: El archivo {self.entrada_path} no existe.'
            return None

    def analizar_sintacticamente(self, tokens):
        # A simple example of syntax checking implementation
        try:
            # Here we should implement the syntax tree validation logic
            pass
        except SyntaxError as e:
            self.error = f'<{e.lineno},{e.offset}> Error sintactico: se encontro: "{e.text.strip()}"; se esperaba: {e.msg}.'

    def generar_reporte(self):
        with open(self.salida_path, 'w', encoding='utf-8') as salida:
            if self.error:
                salida.write(self.error + '\n')
            else:
                salida.write("**El analisis sintactico ha finalizado exitosamente.**\n")

def main():
    carpeta_entradas = ''
    carpeta_salidas = ''
    os.makedirs(carpeta_salidas, exist_ok=True)
    for archivo in os.listdir(carpeta_entradas):
        if archivo.endswith('.py'):
            entrada = os.path.join(carpeta_entradas, archivo)
            salida = os.path.join(carpeta_salidas, f'salida_{archivo.split(".")[0]}.txt')
            analizador = AnalizadorSintactico(entrada, salida)
            code = analizador.leer_archivo()
            if code:
                tokens = lexer(code)
                analizador.analizar_sintacticamente(tokens)
                analizador.generar_reporte()

if __name__ == '__main__':
    main()