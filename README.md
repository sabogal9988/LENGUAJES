# Python Lexical Analyzer

## Descripción

Este proyecto implementa un **analizador léxico** (o lexer) para el lenguaje de programación Python. El objetivo del analizador es descomponer el código fuente de Python en una lista de tokens para facilitar su análisis sintáctico o posterior procesamiento.

El analizador léxico es capaz de reconocer palabras reservadas de Python, operadores, identificadores, literales numéricos y booleanos, cadenas de texto, y comentarios. También detecta errores léxicos cuando encuentra secuencias de caracteres no válidas en el código fuente.

## Características

- **Palabras reservadas:** Reconoce todas las palabras reservadas de Python, como `if`, `else`, `def`, `class`, etc.
- **Operadores booleanos y comparaciones:** Maneja operadores como `and`, `or`, `not`, así como comparaciones (`==`, `!=`, `<`, `<=`, `>=`).
- **Funciones matemáticas:** Detecta funciones matemáticas comunes como `sin`, `cos`, `sqrt`, `pi`, entre otras.
- **Constantes booleanas y numéricas:** Soporta constantes como `True`, `False`, `None`, `pi`, `e`, y `tau`.
- **Identificadores:** Detecta correctamente los nombres de variables y funciones.
- **Números:** Soporta números enteros, flotantes, y notación científica.
- **Cadenas de texto:** Detecta cadenas delimitadas por comillas simples o dobles.
- **Comentarios:** Ignora comentarios de una línea iniciados por `#`.
- **Errores léxicos:** Informa de errores léxicos y detiene el análisis cuando se encuentra un carácter no válido.

## Requisitos

- Python 3.x

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/python-lexical-analyzer.git
   cd python-lexical-analyzer
2. **Crear el entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate  # En Windows

## Ejecucion
Para ejecutar el analizador léxico sobre un archivo de código Python, sigue estos pasos:

1.  Crea o coloca el archivo Python que deseas analizar en el directorio raíz del proyecto. Por ejemplo, crea un archivo llamado codigo_fuente.py con el siguiente contenido:

   ```bash
   class Animal:
      def sound(self):
         return "moo"

   c = Animal()
   print(c.sound())
   ```

2. Ejecuta el analizador léxico:


   ```bash
   python main.py
   ```
   Esto analizará el archivo codigo_fuente.py y generará un archivo de salida output.txt con los tokens generados.

3. Revisar el resultado: Abre el archivo output.txt para ver los tokens generados por el analizador léxico.

Ejemplo de salida en output.txt:

```bash 
<class,1,1>
<id,Animal,1,7>
<tk_dos_puntos,1,13>
<def,2,5>
<id,sound,2,9>
<tk_par_izq,2,14>
<id,self,2,15>
<tk_par_der,2,19>
<tk_dos_puntos,2,20>
<return,3,9>
<tk_cadena,"moo",3,16>
<id,c,5,1>
<tk_asig,5,3>
<id,Animal,5,5>
<tk_par_izq,5,11>
<tk_par_der,5,12>
<print,6,1>
<tk_par_izq,6,6>
<id,c,6,7>
<tk_punto,6,8>
<id,sound,6,9>
<tk_par_izq,6,14>
<tk_par_der,6,15>
<tk_par_der,6,16>
```
## Errores lexicos 

Si el analizador léxico detecta un error léxico, se reportará en el archivo output.txt y el análisis se detendrá. El formato del error es el siguiente:

```bash
>>> Error lexico(linea:X,posicion:Y)
```
Donde X es el número de línea y Y es la posición del error.

## Integrantes

- **Daniel Santiago Varela Guerrero**
- **Miguel Angel Velasco**
- **Sebastian Sabogal Castillo**