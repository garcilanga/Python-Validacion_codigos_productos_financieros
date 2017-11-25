# Validación de códigos ISIN

## ¿Qué es un código ISIN?

- **ISIN** es el acrónimo de **International Securities Identification Numbering system**.
- El código ISIN se utiliza para identificar valores mobiliarios de forma unívoca a nivel internacional y tiene una gran acogida en todos los mercados financieros del mundo, que lo han incorporado a sus procesos de liquidación y custodia.
- Está desarrollado en el estándar internacional ISO 6166.
- Ejemplos de códigos ISIN:
    - LU0363935064
    - ES2766463697

## ¿Qué formato tiene un ISIN?

- Un código ISIN está formado por 12 caracteres alfanuméricos con la siguiente estructura:
    - Los primeros **dos caracteres** corresponden al código del país de la agencia de codificación que asigna el código. La lista de valores posibles está formada por:
        - Códigos de país definidos por la norma ISO-3166 en formato alfanumérico de dos letras:
            - 'AD', 'AE', 'AF', 'AG', 'AI', 'AL', ..., 'ES', ...
        - Códigos de país especiales para valores internacionales:
            - XS, EU
        - Códigos que pueden asignar algunas agencias:
            - XA (CUSIP Global Services)
            - XB (NSD Russia)
            - XC (WM Datenservice Germany)
            - XD (SIX Telekurs)
    - Los siguientes **nueve caracteres** contienen el código nacional de identificación del valor en cada país. La estructura y tamaño de este código quedan al criterio de la agencia de codificación del país.
    - El **último carácter** es un dígito de control.

## Script de ejemplo

- El script Python **isin.py** contiene la clase ISIN para manejar códigos ISIN. Puede importarse en cualquier script Python o ejecutarse directamente para ver algunos ejemplos de prueba, por ejemplo, desde línea de comando:
```
python isin.py
```
- Resultado:
```
- ISIN generado automáticamente                                       : NG0649661241
- El código NG0649661241 ¿es un ISIN válido?                          : True
- El código NG0649661240 ¿es un ISIN válido?                          : False
- Devuelve NG0649661241 si es un código ISIN válido o nada si no lo es: NG0649661241
- Devuelve NG0649661240 si es un código ISIN válido o nada si no lo es: 
- Dígito de control de ISIN para NG0649661241                         : 1
- Dígito de control de ISIN para NG064966124                          : 1
- Dígito de control de ISIN para NG06496612                           : None
- Dígito de control de ISIN para NG0649661240                         : 1
- ISIN de país SH generado automáticamente                            : SH6940885953
- ISIN de país VU y número KQ6PX4B generado automáticamente           : VU00KQ6PX4B0
```
    
## Referencias y más información
- [Código ISIN (wikipedia)](https://es.wikipedia.org/wiki/C%C3%B3digo_ISIN)
- [Library isin.py (github)](https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/isin.py)
- [Consulta de códigos ISIN (CNMV)](https://www.cnmv.es/portal/ancv/ConsultaISIN.aspx)

