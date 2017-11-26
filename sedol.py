#!/usr/bin/env python
# -*- coding: utf-8 -*-
#encoding:utf-8

import pycountry
import random
import re

####################################################################################################
### Clase para validar y gestionar códigos SEDOL
### Stock Exchange Daily Official List for the London Stock Exchange
### https://en.wikipedia.org/wiki/SEDOL
### https://www.rosettacode.org/wiki/SEDOLs
### https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/gb/sedol.py
####################################################################################################

### Caracteres permitidos en un código SEDOL
CTT_SEDOL_CHARACTERS = '0123456789 BCD FGH JKLMN PQRST VWXYZ'
CTT_SEDOL_CHARACTERS = re.sub('\s', '', CTT_SEDOL_CHARACTERS)

class SEDOL:

    ####################################################################################################
    ### Calcula el dígito de control de un código SEDOL
    ####################################################################################################
    def getChecksumSEDOL(self, body):
        if body:
            body = unicode(body).upper()
            if len(body) in (6, 7):
                body = body[:6]
                sedolweight = [1,3,1,7,3,9]
                tmp = sum(map(lambda x, weight: int(str(x), 36) * weight, body, sedolweight) )
                return str((10 - (tmp % 10)) % 10)
        return None

    ####################################################################################################
    ### Determina si un SEDOL es correcto. Retorna True o False
    ####################################################################################################
    def isSEDOL(self, maybeSEDOL):
        return self.getOkSEDOL(maybeSEDOL) != ''

    ####################################################################################################
    ### Determina si un SEDOL es correcto. Retorna SEDOL o ''
    ####################################################################################################
    def getOkSEDOL(self, maybeSEDOL):
        if maybeSEDOL:
            maybeSEDOL = unicode(maybeSEDOL).upper()
            maybeSEDOL = re.sub('\s', '', maybeSEDOL)
            if len(maybeSEDOL) == 7:
                if all(x in CTT_SEDOL_CHARACTERS for x in maybeSEDOL):
                    if self.getChecksumSEDOL(maybeSEDOL[:-1]) == maybeSEDOL[-1]:
                        return maybeSEDOL
        return ''

    ####################################################################################################
    ### Genera un código SEDOL correcto
    ####################################################################################################
    def createSEDOL(self):
        body = ''.join(map(lambda x: random.choice(list(CTT_SEDOL_CHARACTERS)), range(6)))
        control = self.getChecksumSEDOL(body)
        sedol = ''.join([body, control])
        return unicode(sedol)

if __name__ == "__main__":

    mgrsedol = SEDOL()
    sedol = mgrsedol.createSEDOL()
    
    print u'- SEDOL generado automáticamente                                  :', sedol
    print u'- El código %s ¿es un SEDOL válido?                          : %s' % (sedol, mgrsedol.isSEDOL(sedol))
    print u'- El código %s ¿es un SEDOL válido?                          : %s' % (sedol[:-1]+sedol[2], mgrsedol.isSEDOL(sedol[:-1]+sedol[2]))
    print u'- Devuelve %s si es un código SEDOL válido o nada si no lo es: %s' % (sedol, mgrsedol.getOkSEDOL(sedol))
    print u'- Devuelve %s si es un código SEDOL válido o nada si no lo es: %s' % (sedol[:-1]+sedol[2], mgrsedol.getOkSEDOL(sedol[:-1]+sedol[2]))
    print u'- Dígito de control de SEDOL para %s                         : %s' % (sedol, mgrsedol.getChecksumSEDOL(sedol))
    print u'- Dígito de control de SEDOL para %s                          : %s' % (sedol[:-1], mgrsedol.getChecksumSEDOL(sedol[:-1]))
    print u'- Dígito de control de SEDOL para %s                           : %s' % (sedol[:-2], mgrsedol.getChecksumSEDOL(sedol[:-2]))
    print u'- Dígito de control de SEDOL para %s                         : %s' % (sedol[:-1]+sedol[2], mgrsedol.getChecksumSEDOL(sedol[:-1]+sedol[2]))

