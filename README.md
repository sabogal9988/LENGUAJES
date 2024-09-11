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
