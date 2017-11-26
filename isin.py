#!/usr/bin/env python
# -*- coding: utf-8 -*-
#encoding:utf-8

import pycountry
import random
import re

####################################################################################################
### Clase para validar y gestionar códigos ISIN
### ISO 6166 for ISIN code
### https://www.rosettacode.org/wiki/
### https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/isin.py
####################################################################################################

### Caracteres permitidos en un código ISIN
CTT_ISIN_CHARACTERS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

### Lista de países permitidos en códigos ISIN:
### - Lista de países (ISO-3166) en formato de 2 letras
### - Códigos de país XS especiales para valores internacionales.
### - Agencias sustitutos pueden asignar un ISIN comenzando con:
###     - XA (CUSIP Global Services)
###     - XB (NSD Russia)
###     - XC (WM Datenservice Germany)
###     - XD (SIX Telekurs).
CTT_COUNTRIES_LST = map(lambda x: x.alpha_2, list(pycountry.countries)) + [ 'XS', 'EU', 'XA', 'XB', 'XC', 'XD']
CTT_COUNTRIES_LST.sort()

class ISIN:

    ####################################################################################################
    ### Calcula el dígito de control de un código ISIN
    ####################################################################################################
    def getChecksumISIN(self, body):
        if body:
            body = unicode(body).upper()
            if len(body) in (11, 12):
                body = body[:11]
                body = ''.join(str(CTT_ISIN_CHARACTERS.index(n)) for n in body)
                body = ''.join(str((2, 1)[i % 2] * int(n)) for i, n in enumerate(reversed(body)))
                return str((10 - sum(int(n) for n in body)) % 10)
        return None

    ####################################################################################################
    ### Determina si un ISIN es correcto. Retorna True o False
    ####################################################################################################
    def isISIN(self, maybeISIN):
        return self.getOkISIN(maybeISIN) != ''

    ####################################################################################################
    ### Determina si un ISIN es correcto. Retorna ISIN o ''
    ####################################################################################################
    def getOkISIN(self, maybeISIN):
        if maybeISIN:
            maybeISIN = unicode(maybeISIN).upper()
            maybeISIN = re.sub('\s', '', maybeISIN)
            if len(maybeISIN) == 12:
                if all(x in CTT_ISIN_CHARACTERS for x in maybeISIN):
                    if maybeISIN[:2] in CTT_COUNTRIES_LST:
                        if self.getChecksumISIN(maybeISIN[:-1]) == maybeISIN[-1]:
                            return maybeISIN
        return ''

    ####################################################################################################
    ### Genera un código ISIN correcto
    ####################################################################################################
    def createISIN(self, country=None, number=None):
        if not country or country not in CTT_COUNTRIES_LST:
            country = random.choice(CTT_COUNTRIES_LST)
        if not number:
            number = ''.join(map(lambda x: random.choice(list('0123456789')), range(9)))
        else:
            number = ''.join(map(lambda x: '0', range(9-len(number)))) + number
        control = self.getChecksumISIN(''.join([country, number]))
        isin = ''.join([country, number, control])
        return unicode(isin)
    
if __name__ == "__main__":

    mgrisin = ISIN()
    isin = mgrisin.createISIN()
    
    print u'- ISIN generado automáticamente                                       :', isin
    print u'- El código %s ¿es un ISIN válido?                          : %s' % (isin, mgrisin.isISIN(isin))
    print u'- El código %s ¿es un ISIN válido?                          : %s' % (isin[:-1]+isin[2], mgrisin.isISIN(isin[:-1]+isin[2]))
    print u'- Devuelve %s si es un código ISIN válido o nada si no lo es: %s' % (isin, mgrisin.getOkISIN(isin))
    print u'- Devuelve %s si es un código ISIN válido o nada si no lo es: %s' % (isin[:-1]+isin[2], mgrisin.getOkISIN(isin[:-1]+isin[2]))
    print u'- Dígito de control de ISIN para %s                         : %s' % (isin, mgrisin.getChecksumISIN(isin))
    print u'- Dígito de control de ISIN para %s                          : %s' % (isin[:-1], mgrisin.getChecksumISIN(isin[:-1]))
    print u'- Dígito de control de ISIN para %s                           : %s' % (isin[:-2], mgrisin.getChecksumISIN(isin[:-2]))
    print u'- Dígito de control de ISIN para %s                         : %s' % (isin[:-1]+isin[2], mgrisin.getChecksumISIN(isin[:-1]+isin[2]))
    
    country = random.choice(CTT_COUNTRIES_LST)
    isin = mgrisin.createISIN(country)
    print u'- ISIN de país %s generado automáticamente                            : %s' % (country, isin)

    country = random.choice(CTT_COUNTRIES_LST)
    number = ''.join(map(lambda x: random.choice(CTT_ISIN_CHARACTERS), range(7)))
    isin = mgrisin.createISIN(country, number)
    print u'- ISIN de país %s y número %s generado automáticamente           : %s' % (country, number, isin)

