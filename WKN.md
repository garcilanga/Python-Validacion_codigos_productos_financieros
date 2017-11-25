# Validación de códigos WKN

## ¿Qué es un código WKN?

- **WKN** es el acrónimo de **Wertpapier Kenn Nummer**.
- Los códigos WKN son el número nacional de identificación de Valores emitidos en Alemania.
- Ejemplo de código WKN:
    - A0D94M

## ¿Qué formato tiene un WKN?

- Un código Los WKN está formado por 6 caracteres alfanuméricos.

## Script de ejemplo

- El script Python **wkn.py** contiene la clase WKN para manejar códigos WKN. Puede importarse en cualquier script Python o ejecutarse directamente para ver algunos ejemplos de prueba. Por ejemplo, desde línea de comando ejecutar:
```
python wkn.py
```
- Resultado:
```
- WKN generado automáticamente                                 : 82Y573
- El código 82Y573 ¿es un WKN válido?                          : True
- Devuelve 82Y573 si es un código WKN válido o nada si no lo es: 82Y573
- Devuelve 82Y57Y si es un código WKN válido o nada si no lo es: 82Y57Y
```

## Referencias y más información

- [Library wkn.py by arthurdejong](https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/de/wkn.py)
