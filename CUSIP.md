# Validación de códigos CUSIP

## ¿Qué es un código CUSIP?

- **CUSIP** es el acrónimo de **Committee on Uniform Securities Identification Procedures**.
- Los códigos CUSIP son el número de identificación de Valores emitidos en América del Norte (Estados Unidos y Canadá).
- Ejemplos de códigos CUSIP:
    - 780259206

## ¿Qué formato tiene un CUSIP?

- Un código Los CUSIP está formado por 9 caracteres alfanuméricos con la siguiente estructura:
    - Los **seis primeros** caracteres corresponden al código de emisor.
    - Los **dos siguientes** caracteres corresponden al número de edición.
    - El **último caracter** es el dígito de control.

## Script de ejemplo

- El script Python **cusip.py** contiene la clase CUSIP para manejar códigos CUSIP. Puede importarse en cualquier script Python o ejecutarse directamente para ver algunos ejemplos de prueba. Por ejemplo, desde línea de comando ejecutar:
```
python cusip.py
```
- Resultado:
```
- CUSIP generado automáticamente                                    : 6CQ@HDAH5
- El código 6CQ@HDAH5 ¿es un CUSIP válido?                          : True
- El código 6CQ@HDAHQ ¿es un CUSIP válido?                          : False
- Devuelve 6CQ@HDAH5 si es un código CUSIP válido o nada si no lo es: 6CQ@HDAH5
- Devuelve 6CQ@HDAHQ si es un código CUSIP válido o nada si no lo es: 
- Dígito de control de CUSIP para 6CQ@HDAH5                         : 5
- Dígito de control de CUSIP para 6CQ@HDAH                          : 5
- Dígito de control de CUSIP para 6CQ@HDA                           : None
- Dígito de control de CUSIP para 6CQ@HDAHQ                         : 5
```
## Referencias y más información:

- [CUSIP (wikipedia)](https://en.wikipedia.org/wiki/CUSIP)
- [CUSIP (rosettacode)](https://www.rosettacode.org/wiki/CUSIP)
- [Library cusip.py by arthurdejong](https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/cusip.py)
