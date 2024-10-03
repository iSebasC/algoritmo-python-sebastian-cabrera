# Documentación del Algoritmo

## 1. Explicación del Algoritmo

Este programa lee un archivo de texto con URLs y realiza las siguientes tareas:

1. **Lee el archivo línea por línea** para no usar demasiada memoria.
2. **Filtra las URLs** que:
   - Contienen la palabra "shop" en su dominio.
   - Terminan con la extensión `.html`.
3. **Elimina duplicados** usando un conjunto (`set`).
4. **Cuenta cuántas URLs cumplen los criterios** y muestra el resultado.

## 2. Optimización

- **Lectura línea por línea**: Esto permite procesar archivos muy grandes sin problemas de memoria.
- **Uso de set**: Almacena las URLs sin duplicados, haciendo el proceso más rápido y simple.

## 3. Cómo Ejecutar el Programa

1. **Guarda el archivo de texto** con las URLs como `urls.txt` en la misma carpeta que el script de Python.
2. **Corre el script** usando el siguiente comando en la terminal:

   ```bash
   python algoritmo.py
2. **Ver el resultado** El programa mostrará cuantas URLs cumplen los criterios y luego listará esas URLs.

