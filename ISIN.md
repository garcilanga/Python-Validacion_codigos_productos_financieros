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
        - Códigos de país especiales para valores internacionales.
            - XS, EU
        - Códigos que pueden asignar algunas agencias:
            - XA (CUSIP Global Services)
            - XB (NSD Russia)
            - XC (WM Datenservice Germany)
            - XD (SIX Telekurs)
    - Los siguientes **nueve caracteres** contienen el código nacional de identificación del valor en cada país. La estructura y tamaño de este código quedan al criterio de la agencia de codificación del país.
    - El **último carácter** es un dígito de control.
    
