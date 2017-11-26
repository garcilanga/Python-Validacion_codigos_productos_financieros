#!/usr/bin/env python
# -*- coding: utf-8 -*-
#encoding:utf-8

import pycountry
import random
import re

####################################################################################################
### Clase para validar y gestionar códigos WKN
### Wertpapier Kenn-Nummer, the alphanumeric German identification number
### https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/de/wkn.py
####################################################################################################

### Caracteres permitidos en un código WKN
CTT_WKN_CHARACTERS = u'0123456789ABCDEFGH JKLMN PQRSTUVWXYZ'
CTT_WKN_CHARACTERS = re.sub('\s', '', CTT_WKN_CHARACTERS)

class WKN:

    ####################################################################################################
    ### Determina si un WKN es correcto. Retorna True o False
    ####################################################################################################
    def isWKN(self, maybeWKN):
        return self.getOkWKN(maybeWKN) != ''

    ####################################################################################################
    ### Determina si un WKN es correcto. Retorna WKN o ''
    ####################################################################################################
    def getOkWKN(self, maybeWKN):
        if maybeWKN:
            maybeWKN = unicode(maybeWKN).upper()
            maybeWKN = re.sub('\s', '', maybeWKN)
            if len(maybeWKN) == 6:
                if all(x in CTT_WKN_CHARACTERS for x in maybeWKN):
                    return maybeWKN
        return ''

    ####################################################################################################
    ### Genera un código WKN correcto
    ####################################################################################################
    def createWKN(self):
        wkn = ''.join(map(lambda x: random.choice(list(CTT_WKN_CHARACTERS)), range(6)))
        return unicode(wkn)

if __name__ == "__main__":

    mgrwkn = WKN()
    wkn = mgrwkn.createWKN()
    
    print u'- WKN generado automáticamente                                 :', wkn
    print u'- El código %s ¿es un WKN válido?                          : %s' % (wkn, mgrwkn.isWKN(wkn))
    print u'- Devuelve %s si es un código WKN válido o nada si no lo es: %s' % (wkn, mgrwkn.getOkWKN(wkn))
    print u'- Devuelve %s si es un código WKN válido o nada si no lo es: %s' % (wkn[:-1]+wkn[2], mgrwkn.getOkWKN(wkn[:-1]+wkn[2]))
    
