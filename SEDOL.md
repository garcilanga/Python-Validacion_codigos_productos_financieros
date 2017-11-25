# Validación de códigos SEDOL

## ¿Qué es un código SEDOL?

- **SEDOL** es el acrónimo de **Stock Exchange Daily Official List**.
- Los códigos SEDOL son el Número Nacional de Identificación de Valores emitidos en el Reino Unido e Irlanda.
- Ejemplo de código SEDOL:
    - B03MLX2

## ¿Qué formato tiene un SEDOL?

- Un código Los SEDOL está formado por 7 caracteres alfanuméricos con la siguiente estructura: 
    - Los primeros **seis caracteres** son un código alfanumérico.
    - El **último carácter** es un dígito de control.

## Script de ejemplo

- El script Python **sedol.py** contiene la clase SEDOL para manejar códigos SEDOL. Puede importarse en cualquier script Python o ejecutarse directamente para ver algunos ejemplos de prueba. Por ejemplo, desde línea de comando ejecutar:
```
python sedol.py
```
- Resultado:
```
- SEDOL generado automáticamente                                  : J5ND0M4
- El código J5ND0M4 ¿es un SEDOL válido?                          : True
- El código J5ND0MN ¿es un SEDOL válido?                          : False
- Devuelve J5ND0M4 si es un código SEDOL válido o nada si no lo es: J5ND0M4
- Devuelve J5ND0MN si es un código SEDOL válido o nada si no lo es: 
- Dígito de control de SEDOL para J5ND0M4                         : 4
- Dígito de control de SEDOL para J5ND0M                          : 4
- Dígito de control de SEDOL para J5ND0                           : None
- Dígito de control de SEDOL para J5ND0MN                         : 4
```

## Referencias y más información

- [SEDOL (Wikipedia)](https://en.wikipedia.org/wiki/SEDOL)
- [SEDOLs (www.rosettacode.org)](https://www.rosettacode.org/wiki/SEDOLs)
- [Library sedol.py by arthurdejong](https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/gb/sedol.py)
